import pandas as pd

# Ensure you have pyarrow installed
# pip install pyarrow

df = pd.read_parquet(r"C:\Users\rawat\Downloads\green_tripdata_2024-01.parquet")
print(df.head())
print(df.shape)