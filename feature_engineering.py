import pandas as pd
import numpy as np
import os

# Load dataset
data = pd.read_csv("data/customer_churn_data.csv")

print("Original dataset shape:", data.shape)

# -------------------------------
# Data Cleaning
# -------------------------------

# Remove duplicate customers
data = data.drop_duplicates(subset="customer_id")

# Handle missing numerical values
numeric_columns = data.select_dtypes(include=np.number).columns

for column in numeric_columns:
    data[column] = data[column].fillna(data[column].median())

# Handle missing categorical values
categorical_columns = data.select_dtypes(include="object").columns

for column in categorical_columns:
    data[column] = data[column].fillna(data[column].mode()[0])

# -------------------------------
# Feature Engineering
# -------------------------------

# RFM - Recency
data["recency"] = data["last_login_days"]

# RFM - Frequency
data["frequency"] = data["logins_last_30_days"]

# RFM - Monetary
data["monetary"] = data["mrr"]

# Engagement velocity / delta
data["engagement_change"] = (
    data["logins_last_7_days"]
    - (data["logins_last_30_days"] / 4)
)

# Support Friction Index
data["support_friction_index"] = (
    data["open_support_tickets"]
    * data["avg_resolution_time_hours"]
)

# Inactivity streak
data["inactivity_streak"] = np.maximum(
    data["last_login_days"] - 7,
    0
)

# -------------------------------
# Save processed dataset
# -------------------------------

output_path = "data/processed_churn_data.csv"

data.to_csv(output_path, index=False)

print("Feature engineering completed successfully!")
print("Final dataset shape:", data.shape)
print("Saved at:", output_path)

print("\nFinal columns:")
print(data.columns.tolist())

print("\nFirst 5 rows:")
print(data.head())