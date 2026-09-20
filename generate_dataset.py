import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

data = pd.DataFrame({
    "customer_id": [f"CUST{i:04d}" for i in range(1, n + 1)],

    # Demographic & Account Data
    "industry": np.random.choice(
        ["Technology", "Healthcare", "Finance", "Retail", "Education"],
        n
    ),
    "company_size": np.random.choice(
        ["Small", "Medium", "Large"],
        n
    ),
    "geography": np.random.choice(
        ["India", "USA", "UK", "Canada", "Australia"],
        n
    ),
    "subscription_tier": np.random.choice(
        ["Basic", "Professional", "Enterprise"],
        n
    ),
    "tenure_months": np.random.randint(1, 61, n),

    # Financial & Billing Data
    "mrr": np.round(np.random.uniform(20, 2000, n), 2),
    "billing_frequency": np.random.choice(
        ["Monthly", "Annual"],
        n,
        p=[0.7, 0.3]
    ),
    "discount_used": np.random.choice(
        [0, 1],
        n,
        p=[0.65, 0.35]
    ),
    "payment_delays": np.random.randint(0, 6, n),

    # Product Telemetry
    "daily_active_users": np.random.randint(1, 100, n),
    "feature_adoption_rate": np.round(
        np.random.uniform(0.05, 1.0, n), 2
    ),
    "avg_session_length": np.round(
        np.random.uniform(2, 90, n), 2
    ),
    "time_to_value_days": np.random.randint(1, 61, n),

    # Customer Support
    "open_support_tickets": np.random.randint(0, 10, n),
    "avg_resolution_time_hours": np.round(
        np.random.uniform(1, 120, n), 2
    ),
    "nps_score": np.random.randint(-100, 101, n),
    "support_sentiment": np.round(
        np.random.uniform(-1, 1, n), 2
    ),

    # Engagement
    "last_login_days": np.random.randint(0, 60, n),
    "logins_last_7_days": np.random.randint(0, 30, n),
    "logins_last_30_days": np.random.randint(0, 120, n),

    # Target
    "churn": np.random.choice(
        [0, 1],
        n,
        p=[0.92, 0.08]
    )
})

# Create engagement delta feature
data["engagement_delta"] = (
    data["logins_last_7_days"] -
    (data["logins_last_30_days"] / 4)
)

# Create inactivity streak
data["inactivity_streak"] = np.maximum(
    data["last_login_days"] - 7,
    0
)

# Create Support Friction Index
data["support_friction_index"] = (
    data["open_support_tickets"] *
    data["avg_resolution_time_hours"]
)# Save dataset
import os

# Get the folder where this Python file is located
project_folder = os.path.dirname(os.path.abspath(__file__))

# Create data folder if it does not exist
data_folder = os.path.join(project_folder, "data")
os.makedirs(data_folder, exist_ok=True)

# Create complete file path
file_path = os.path.join(data_folder, "customer_churn_data.csv")

# Save dataset
data.to_csv(file_path, index=False)

print("Dataset created successfully!")
print("Shape:", data.shape)
print("Saved at:", file_path)
print(data.head())

