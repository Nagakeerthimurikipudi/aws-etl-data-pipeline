def lambda_handler(event, context):
    print("Lambda triggered ETL job")
    # In real AWS, this would start Glue job via boto3
    # Simulated here
    import subprocess
    subprocess.run(["python", "etl_glue_job.py"])
    print("ETL job triggered by Lambda")
