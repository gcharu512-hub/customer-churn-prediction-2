import streamlit as st
import pandas as pd
import os

# Page configuration
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Customer Churn Prediction Dashboard")
st.write("Analyze customer data and understand churn-related patterns.")

# Dataset path
DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "data",
    "customer_churn_data.csv"
)

# Check whether dataset exists
if not os.path.exists(DATA_PATH):
    st.error("❌ Dataset file not found!")
    st.write("Expected location:")
    st.code(DATA_PATH)
    st.stop()

# Load dataset
try:
    data = pd.read_csv(DATA_PATH)
except Exception as e:
    st.error("❌ Error while reading the dataset.")
    st.write(e)
    st.stop()

# Sidebar
st.sidebar.header("Dashboard Menu")

page = st.sidebar.selectbox(
    "Select Section",
    [
        "Overview",
        "Customer Data",
        "Churn Analysis",
        "Feature Analysis"
    ]
)

# ---------------- OVERVIEW ----------------

if page == "Overview":

    st.header("📌 Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Customers", len(data))

    with col2:
        st.metric("Total Features", len(data.columns))

    # Find churn column automatically
    churn_column = None

    for col in data.columns:
        if col.lower() in ["churn", "churned", "is_churn", "customer_churn"]:
            churn_column = col
            break

    if churn_column is not None:
        churn_values = data[churn_column].astype(str).str.lower()

        churn_count = churn_values.isin(
            ["yes", "1", "true", "churn", "churned"]
        ).sum()

        churn_rate = (churn_count / len(data)) * 100

        with col3:
            st.metric("Churned Customers", int(churn_count))

        with col4:
            st.metric("Churn Rate", f"{churn_rate:.2f}%")

    else:
        with col3:
            st.metric("Missing Values", int(data.isnull().sum().sum()))

        with col4:
            st.metric("Duplicate Rows", int(data.duplicated().sum()))

    st.subheader("Dataset Preview")
    st.dataframe(data.head(10), use_container_width=True)

    st.subheader("Dataset Information")

    info_df = pd.DataFrame({
        "Column": data.columns,
        "Data Type": data.dtypes.astype(str),
        "Missing Values": data.isnull().sum().values
    })

    st.dataframe(info_df, use_container_width=True)


# ---------------- CUSTOMER DATA ----------------

elif page == "Customer Data":

    st.header("👥 Customer Data")

    st.write(f"Dataset contains **{len(data)} customers**.")

    st.dataframe(
        data,
        use_container_width=True,
        height=500
    )


# ---------------- CHURN ANALYSIS ----------------

elif page == "Churn Analysis":

    st.header("📈 Churn Analysis")

    churn_column = None

    for col in data.columns:
        if col.lower() in ["churn", "churned", "is_churn", "customer_churn"]:
            churn_column = col
            break

    if churn_column is None:

        st.warning(
            "No standard churn column was found in the dataset."
        )

        st.write("Available columns:")
        st.write(list(data.columns))

    else:

        churn_counts = data[churn_column].value_counts()

        st.subheader("Churn Distribution")

        st.bar_chart(churn_counts)

        st.subheader("Churn Statistics")

        st.dataframe(
            churn_counts.rename("Customers"),
            use_container_width=True
        )


# ---------------- FEATURE ANALYSIS ----------------

elif page == "Feature Analysis":

    st.header("🔎 Feature Analysis")

    numeric_columns = data.select_dtypes(
        include="number"
    ).columns.tolist()

    if len(numeric_columns) == 0:

        st.warning("No numerical columns found.")

    else:

        selected_feature = st.selectbox(
            "Select a numerical feature",
            numeric_columns
        )

        st.subheader(
            f"Distribution of {selected_feature}"
        )

        st.bar_chart(
            data[selected_feature].value_counts().sort_index()
        )

        st.subheader("Statistics")

        stats = data[selected_feature].describe()

        st.dataframe(
            stats.to_frame("Value"),
            use_container_width=True
        )


# Footer
st.sidebar.markdown("---")
st.sidebar.info(
    "Customer Churn Prediction Project"
)