import os
import pandas as pd
import numpy as np
import datetime as dt

# Ensure directories exist
os.makedirs('analytics_engine/data', exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

# Generate Mock Data
n_rows = 150
customer_ids = [f"CUST-{i:04d}" for i in np.random.randint(1001, 1050, n_rows)]

# Generate random dates over the last 90 days
start_date = dt.datetime(2026, 3, 1)
end_date = dt.datetime(2026, 5, 31)
random_dates = [start_date + dt.timedelta(days=int(np.random.randint(0, 90))) for _ in range(n_rows)]

# Generate random purchase amounts (skewed to simulate normal vs VIP spend)
amounts = np.round(np.random.exponential(scale=150, size=n_rows) + 10, 2)

# Create DataFrame
df = pd.DataFrame({
    'CustomerID': customer_ids,
    'InvoiceDate': random_dates,
    'TransactionAmount': amounts
})

# Save to your new data folder
df.to_csv('analytics_engine/data/transactions.csv', index=False)
print("✅ Mock dataset generated successfully at analytics_engine/data/transactions.csv!")
