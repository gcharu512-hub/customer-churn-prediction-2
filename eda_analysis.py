import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv("data/customer_churn_data.csv")

# Create graph folder
os.makedirs("outputs/graphs", exist_ok=True)

print("Dataset loaded successfully!")
print("Shape:", df.shape)

# ============================================================
# 1. CHURN DISTRIBUTION
# ============================================================

plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="churn")
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("outputs/graphs/churn_distribution.png", dpi=300)
plt.show()


# ============================================================
# 2. CHURN BY BILLING
# ============================================================

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="billing_frequency", hue="churn")
plt.title("Churn by Billing Frequency")
plt.xlabel("Billing Frequency")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("outputs/graphs/churn_by_billing.png", dpi=300)
plt.show()


# ============================================================
# 3. CHURN BY INDUSTRY
# ============================================================

plt.figure(figsize=(9, 5))
sns.countplot(data=df, x="industry", hue="churn")
plt.title("Churn by Industry")
plt.xlabel("Industry")
plt.ylabel("Number of Customers")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("outputs/graphs/churn_by_industry.png", dpi=300)
plt.show()


# ============================================================
# 4. CHURN BY SUBSCRIPTION
# ============================================================

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="subscription_tier", hue="churn")
plt.title("Churn by Subscription Tier")
plt.xlabel("Subscription Tier")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("outputs/graphs/churn_by_subscription.png", dpi=300)
plt.show()


# ============================================================
# 5. FEATURE ADOPTION VS CHURN
# ============================================================

plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df,
    x="churn",
    y="feature_adoption_rate"
)
plt.title("Feature Adoption Rate vs Churn")
plt.xlabel("Churn")
plt.ylabel("Feature Adoption Rate")
plt.tight_layout()
plt.savefig("outputs/graphs/feature_adoption_vs_churn.png", dpi=300)
plt.show()


# ============================================================
# 6. MONTHLY REVENUE VS CHURN
# ============================================================

revenue_columns = [
    "mr",
    "monthly_revenue",
    "mrr",
    "revenue"
]

revenue_column = None

for column in revenue_columns:
    if column in df.columns:
        revenue_column = column
        break

if revenue_column:

    plt.figure(figsize=(8, 5))

    sns.boxplot(
        data=df,
        x="churn",
        y=revenue_column
    )

    plt.title("Monthly Revenue vs Churn")
    plt.xlabel("Churn")
    plt.ylabel("Monthly Revenue")

    plt.tight_layout()

    plt.savefig(
        "outputs/graphs/mr_vs_churn.png",
        dpi=300
    )

    plt.show()

else:
    print("Monthly revenue column not found.")


# ============================================================
# 7. SUPPORT FRICTION VS CHURN
# ============================================================

plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df,
    x="churn",
    y="support_friction_index"
)
plt.title("Support Friction Index vs Churn")
plt.xlabel("Churn")
plt.ylabel("Support Friction Index")
plt.tight_layout()
plt.savefig("outputs/graphs/support_friction_vs_churn.png", dpi=300)
plt.show()


# ============================================================
# FINISHED
# ============================================================

print("\n========================================")
print("EDA GRAPHS CREATED SUCCESSFULLY!")
print("========================================")

print("\nCheck the folder:")
print("outputs/graphs/")