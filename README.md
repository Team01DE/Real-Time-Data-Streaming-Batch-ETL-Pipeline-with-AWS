# Real-Time-Data-Streaming-Batch-ETL-Pipeline-with-AWS
Hybrid Architecture for Scalable Analytics


## Overview
This project implements a hybrid data pipeline using AWS services to address common business challenges in e-commerce, IoT, and financial sectors. The pipeline processes real-time streaming data for immediate decision-making (e.g., personalized recommendations, fraud detection) and batches data into a data warehouse for historical trend analysis (e.g., daily sales reports). 

## It tackles:
**Delayed Insights:** Enables sub-second processing of streaming data.

**Data Volume & Velocity:** Efficiently handles large, high-speed data streams.

**Inefficient ETL & Storage:** Optimizes processing and storage with a hybrid approach.

**Poor Data Integration & Scalability:** Unifies real-time and batch analytics in a scalable system.

## Architecture
**Real-Time Ingestion:** AWS Kinesis Data Streams ingests simulated data (e.g., e-commerce transactions, IoT sensor readings).

**Real-Time Processing:** AWS Lambda filters and enriches data, storing it in Amazon S3.

**Batch ETL:** AWS Glue transforms S3 data into a structured format (e.g., Parquet) for analytics.

**Storage:** Amazon S3 for raw and processed data; optionally, Amazon Redshift for querying.

## Prerequisites
**AWS Account:** Access to Kinesis, Lambda, S3, Glue, and optionally Redshift.

**Python 3.x:** For scripting producers and Lambda/Glue functions.

**AWS CLI:** Configured with your credentials (aws configure).

**Boto3:** AWS SDK for Python (pip install boto3).

**Git:** To clone and manage this repository.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or contributions, reach out via GitHub Issues.
