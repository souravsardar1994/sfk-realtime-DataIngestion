
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

## 🌟 Key Snowpipe Concepts

- **Stage**  
  A reference to your data location (e.g., an S3 bucket or prefix). Stages point Snowflake at where files land so it knows what to ingest.

- **File Format**  
  Defines how Snowflake should parse incoming files (CSV, JSON, Parquet, etc.). You can customize delimiters, header handling, compression, and more.

- **Pipe**  
  A named Snowflake object (`CREATE PIPE … AS COPY INTO …`) that ties a stage and file format together. When auto-ingest is enabled, the pipe watches your notification channel and executes the COPY for you.

- **AUTO_INGEST**  
  A pipe parameter that tells Snowpipe to listen for external notifications (SQS, Azure Event Grid, GCS Pub/Sub) instead of requiring manual `ALTER PIPE … REFRESH` calls.

- **Notification Integration**  
  A Snowflake object (`CREATE NOTIFICATION INTEGRATION`) that holds credentials and ARNs for your cloud queue (e.g., AWS SQS). It grants Snowflake permission to poll events.

- **Continuous Ingestion**  
  The overall pattern of detecting new files as they arrive, then loading them immediately. Latency is typically under 1–2 minutes.

- **COPY_HISTORY / LOAD_HISTORY**  
  System views you can query to see what files were loaded, when, and whether they succeeded or failed.

- **Partitioning & Path Patterns**  
  Organize data in your bucket by date or other attributes (e.g., `/year=2025/month=07/`) so Snowpipe copies only the relevant subset and you can purge old data more easily.

---

