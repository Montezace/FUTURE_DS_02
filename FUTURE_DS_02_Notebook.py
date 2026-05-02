# ==============================
# SETUP
# ==============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from IPython.display import display, clear_output
import ipywidgets as widgets

sns.set_style("whitegrid")

# ==============================
# SAMPLE DATA (you can replace this later)
# ==============================
np.random.seed(42)

n = 500
df = pd.DataFrame({
    "customer_id": range(1, n+1),
    "tenure": np.random.randint(1, 60, n),
    "monthly_charges": np.random.uniform(20, 120, n),
    "total_charges": np.random.uniform(100, 5000, n),
    "contract_type": np.random.choice(["Month-to-month", "One year", "Two year"], n),
    "churn": np.random.choice([0, 1], n, p=[0.7, 0.3])
})

# ==============================
# FUNCTION: GENERATE REPORT
# ==============================
def generate_churn_report(b):
    clear_output(wait=True)
    
    display(title)
    display(button)
    
    print("📊 Generating Churn Analysis Report...\n")
    
    churn_rate = df["churn"].mean()
    print(f"Overall Churn Rate: {churn_rate:.2%}")
    
    # --------------------------
    # CHURN BY CONTRACT TYPE
    # --------------------------
    plt.figure()
    contract_churn = df.groupby("contract_type")["churn"].mean().sort_values()
    contract_churn.plot(kind="bar")
    plt.title("Churn Rate by Contract Type")
    plt.ylabel("Churn Rate")
    plt.show()
    
    # --------------------------
    # TENURE VS CHURN
    # --------------------------
    plt.figure()
    sns.boxplot(x="churn", y="tenure", data=df)
    plt.title("Tenure vs Churn")
    plt.show()
    
    # --------------------------
    # MONTHLY CHARGES VS CHURN
    # --------------------------
    plt.figure()
    sns.boxplot(x="churn", y="monthly_charges", data=df)
    plt.title("Monthly Charges vs Churn")
    plt.show()
    
    # --------------------------
    # SUMMARY INSIGHTS
    # --------------------------
    print("📌 Key Insights:")
    
    high_churn_contract = contract_churn.idxmax()
    print(f"- Highest churn occurs in: {high_churn_contract}")
    
    avg_tenure_churn = df[df["churn"] == 1]["tenure"].mean()
    avg_tenure_nochurn = df[df["churn"] == 0]["tenure"].mean()
    
    print(f"- Avg tenure (churned): {avg_tenure_churn:.1f}")
    print(f"- Avg tenure (retained): {avg_tenure_nochurn:.1f}")
    
    print("\n✅ Report Complete")

# ==============================
# UI COMPONENTS
# ==============================
title = widgets.HTML("<h2>Customer Churn Dashboard</h2>")

button = widgets.Button(
    description="Generate Report",
    button_style="success"
)

button.on_click(generate_churn_report)

# ==============================
# DISPLAY UI
# ==============================
display(title)
display(button)
