import pandas as pd
import os

# Simulate AWS Glue Job
print("Starting Glue ETL job...")

input_path = "input/users.csv"
df = pd.read_csv(input_path)

# Transformation logic
summary = df.groupby("country")["purchase_amount"].sum().reset_index()
summary.columns = ["country", "total_purchase"]

output_path = "output/users_summary.csv"
os.makedirs("output", exist_ok=True)
summary.to_csv(output_path, index=False)

print("Glue ETL job completed. Output written to:", output_path)
