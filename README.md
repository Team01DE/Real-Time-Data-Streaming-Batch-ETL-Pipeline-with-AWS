# Real-Time Batch ETL Pipeline for E-Commerce Price Drop Prediction

---

## 🛠️ Project Overview

This project implements a real-time and batch ETL pipeline for monitoring and predicting product price drops in the e-commerce domain. The architecture is fully cloud-native, integrating Docker, AWS services, machine learning, and Power BI to deliver scalable and real-time business intelligence.

---

## 🏗️ Architecture Diagram

![Architecture]([architecture.png](https://github.com/Team01DE/Real-Time-Data-Streaming-Batch-ETL-Pipeline-with-AWS/blob/main/images/architecture.png?raw=true))

---

## ⚙️ Technologies Used

- **Docker** – Real-time producer for streaming product data
- **AWS S3** – Cloud storage for raw and cleaned data
- **AWS Glue** – Schema detection, data cleaning, ETL transformation
- **Amazon Athena** – Serverless SQL querying directly on S3
- **Power BI** – Live dashboards using ODBC connection to Athena
- **AWS EC2** – Hosting a Streamlit-based ML web application
- **Streamlit** – Real-time prediction application
- **Python** – Scripting and machine learning model building
- **Scikit-learn** – Random Forest model for price drop prediction

---

## 🔥 Key Features

- Real-time ingestion of e-commerce product data into S3
- Automated cleaning and schema detection with AWS Glue
- Live SQL querying with Amazon Athena
- Power BI live dashboards connected through ODBC
- ML model prediction of potential price drops (Random Forest Classifier)
- Streamlit web app deployed on EC2 for interactive predictions

---

## 📈 Dashboards and Screenshots

| Feature | Screenshot |
|:--------|:------------|
| Power BI Dashboard (Price Drop Trends, Top Categories) | ![Dashboard](dashboard1.png) |
| Streamlit ML Prediction App | ![Streamlit App](streamlit_app.png) |

---

## 🚀 How to Run

1. **Docker Producer**
   - Navigate to the `docker_producer/` folder.
   - Run the producer to send live data into S3.

2. **AWS Setup**
   - Configure AWS Glue Crawlers and ETL Jobs to transform raw S3 data.
   - Query the cleaned data using Amazon Athena.

3. **Visualization**
   - Set up ODBC connection from Power BI to Athena.
   - Create real-time dashboards and KPIs.

4. **Machine Learning App**
   - Train the model (Random Forest).
   - Deploy the Streamlit app to AWS EC2.
   - Access real-time predictions via the web app.

---

## ✍️ Team Members

- Stuti Bimali
- Priyanka Singh
- Lakshman Rajith (University of New Haven)

---

## 📚 References

- [AWS Glue Documentation](https://docs.aws.amazon.com/glue/)
- [Amazon Athena Documentation](https://docs.aws.amazon.com/athena/)
- [Docker Official Site](https://www.docker.com/resources/what-container/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Power BI Documentation](https://learn.microsoft.com/en-us/power-bi/)
- Khanna, A., & Rani, R. (2019). *Predictive Analytics in E-commerce: Machine Learning Approaches.* Procedia Computer Science.
- Srivastava, S., & Sharma, S. (2020). *Data Visualization Techniques and Tools for Business Intelligence.* International Journal of Management Studies.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
