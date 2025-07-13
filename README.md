### 📌 Project Goal:
To build a cloud-native ETL data pipeline that reads raw purchase data from Amazon S3, transforms it using AWS Glue, stores the processed data back in S3, and analyzes the result using Amazon Athena — with the entire pipeline orchestrated and monitored using AWS Lambda and CloudWatch.

### 🧪 Use Case:
The business wants to track total purchases by country from user transactions. Raw data lands in S3, and the goal is to transform and summarize it so it can be queried directly for reporting.

### 🚀 AWS Services Used:
- **Amazon S3** – to store input and output CSV files (raw and processed data)
- **AWS Glue** – for transformation logic using Python (ETL job)
- **AWS Lambda** – to trigger the Glue job
- **Amazon CloudWatch** – to monitor ETL process, logs, and errors
- **Amazon Athena** – to query the final dataset stored in S3

### 🧱 Architecture Flow:
1. **Input**: Raw CSV data is uploaded to S3 (here, simulated via `input/` folder)
2. **Trigger**: Lambda function gets triggered manually/scheduled
3. **ETL**: Lambda calls Glue Job, which transforms the data (grouping total purchases by country)
4. **Output**: Transformed data is saved back to S3 (`output/` folder in this case)
5. **Query**: Athena reads from the output S3 bucket and performs analysis (like top countries by purchase)
6. **Monitoring**: CloudWatch tracks logs for Glue and Lambda

### 🤔 Why Glue is Used (vs Lambda alone)?
- Glue is purpose-built for **scalable ETL** — supports Spark (PySpark), big datasets, job scheduling
- While Lambda can run Python scripts, it’s limited by time (15 min) and memory (up to 3 GB)
- For real data pipelines, especially with growing data, **Glue is the preferred and scalable choice**

### 📂 Files in This Repo:
- `input/users.csv`: Raw purchase data
- `etl_glue_job.py`: Python transformation logic (used by Glue)
- `output/users_summary.csv`: Final output after aggregation
- `lambda_trigger.py`: Lambda simulation script
- `query_results_athena.sql`: Athena SQL for querying final data
- `cloudwatch_notes.md`: Notes on monitoring jobs with CloudWatch
- `requirements.txt`: Required packages

### ✅ Technologies:
Python, AWS Glue, Lambda, CloudWatch, Athena, S3 (conceptually)
