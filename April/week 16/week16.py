import pandas as pd
import numpy as np
from kaggle.api.kaggle_api_extended import KaggleApi
import os

# Initialize Kaggle API
api = KaggleApi()
api.authenticate()

# Download dataset from Kaggle
# Example: IoT sensor dataset
dataset_name = "garystafford/environmental-sensor-data-132k"
download_path = "./April/week 16/"

print("Downloading dataset from Kaggle...")
api.dataset_download_files(dataset_name, path=download_path, unzip=True)

# Load the CSV file
csv_file = os.path.join(download_path, "iot_telemetry_data.csv")
df = pd.read_csv(csv_file)

print("\n=== Dataset Info ===")
print(df.info())
print("\n=== First few rows ===")
print(df.head())

# Check for missing values
print("\n=== Missing Values ===")
print(df.isnull().sum())

# Handle missing values
# Option 1: Fill with mean for numerical columns
numerical_cols = df.select_dtypes(include=[np.number]).columns
for col in numerical_cols:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].mean(), inplace=True)
        print(f"Filled missing values in {col} with mean")

# Option 2: Fill with mode for categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].mode()[0], inplace=True)
        print(f"Filled missing values in {col} with mode")

# Detect and handle outliers using IQR method
print("\n=== Handling Outliers ===")
for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    if len(outliers) > 0:
        print(f"{col}: Found {len(outliers)} outliers")
        # Cap outliers at bounds
        df[col] = df[col].clip(lower=lower_bound, upper=upper_bound)

# Save cleaned data
cleaned_file = os.path.join(download_path, "cleaned_data.csv")
df.to_csv(cleaned_file, index=False)
print(f"\n=== Cleaned data saved to {cleaned_file} ===")

# Display summary statistics
print("\n=== Summary Statistics ===")
print(df.describe())
