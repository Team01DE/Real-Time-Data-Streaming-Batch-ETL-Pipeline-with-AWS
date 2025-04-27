import requests
import boto3
import json
import csv
import os
import random
from datetime import datetime

# ✅ Use environment variables
bucket_name = os.getenv("AWS_S3_BUCKET", "ecommerce-price-drop-pipeline")
s3_prefix = "price-stream/"
region = os.getenv("AWS_DEFAULT_REGION", "us-east-1")

# ✅ Initialize S3 client
s3 = boto3.client("s3", region_name=region)

def fetch_products():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ Failed to fetch products: {response.status_code}")
        return []

def create_csv(products):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rows = []

    for p in products:
        pid = str(p["id"])
        current_price = float(p["price"])

        # 🧪 Simulate old price (5% to 50% higher)
        simulated_old_price = round(current_price * random.uniform(1.05, 1.5), 2)
        percent_drop = round((simulated_old_price - current_price) / simulated_old_price * 100, 2)
        price_drop = percent_drop > 10

        rows.append({
            "id": pid,
            "title": p["title"],
            "category": p["category"],
            "price": current_price,
            "old_price": simulated_old_price,
            "price_drop": price_drop,
            "percent_drop": percent_drop,
            "timestamp": timestamp
        })

    return rows

def upload_to_s3(rows):
    filename = f"price_batch_{datetime.now().strftime('%Y%m%d%H%M')}.csv"
    fieldnames = ["id", "title", "category", "price", "old_price", "price_drop", "percent_drop", "timestamp"]

    with open(filename, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    with open(filename, "r", encoding='utf-8') as f:
        s3.put_object(Bucket=bucket_name, Key=s3_prefix + filename, Body=f.read())
    
    print(f"✅ Uploaded to S3: s3://{bucket_name}/{s3_prefix + filename}")
    os.remove(filename)

def main():
    print("🚀 Fetching and simulating price drop data...")
    products = fetch_products()
    if not products:
        return
    rows = create_csv(products)
    upload_to_s3(rows)
    print("✅ Upload complete.")

if __name__ == "__main__":
    main()
