
# ⛄ Real-time Ingestion using Snowpipe

This project demonstrates how to implement **real-time data ingestion** into **Snowflake** using **Snowpipe**, 
Snowflake’s continuous data ingestion service. Snowpipe allows data to be loaded automatically as soon as it lands in a stage (internal or external, 
such as AWS S3 or Azure Blob Storage).

---

## 📌 Overview

**Snowpipe** automates the loading of data into Snowflake tables in near real-time using event notifications from cloud providers like AWS S3 or Azure. 
This reduces manual overhead and enables low-latency ingestion pipelines for streaming or micro-batch use cases.

---


## 🧩 Components Used

- **Amazon S3** — Storage layer where data lands
- **Amazon SNS** — Publishes S3 event notifications
- **Amazon SQS** — Subscribes to SNS topic; Snowflake polls this queue
- **Snowflake** — Target data warehouse
- **Snowpipe** — Service that listens for file drops and loads data automatically

---

