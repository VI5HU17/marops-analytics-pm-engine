import pandas as pd
import datetime as dt

def run_rfm_analysis():
    # 1. Load transaction data
    try:
        data = pd.read_csv('analytics_engine/data/transactions.csv')
    except FileNotFoundError:
        print("❌ Error: transactions.csv not found. Please run generate_data.py first.")
        return

    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

    # Establish an operational snapshot date to calculate recency accurately
    snapshot_date = dt.datetime(2026, 6, 1)

    # 2. Aggregate metrics per customer
    rfm = data.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (snapshot_date - x.max()).days, # Recency
        'CustomerID': 'count',                                   # Frequency
        'TransactionAmount': 'sum'                               # Monetary
    })

    rfm.rename(columns={
        'InvoiceDate': 'Recency', 
        'CustomerID': 'Frequency', 
        'TransactionAmount': 'Monetary'
    }, inplace=True)

    # 3. Score scoring metrics (1 to 4 stars based on quartiles)
    # Lower recency is better (bought recently) -> gets a higher score
    rfm['R_Score'] = pd.qcut(rfm['Recency'], 4, labels=[4, 3, 2, 1])
    rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 4, labels=[1, 2, 3, 4])
    rfm['M_Score'] = pd.qcut(rfm['Monetary'], 4, labels=[1, 2, 3, 4])

    # Convert categories back to integers for calculation
    rfm['Total_Score'] = rfm['R_Score'].astype(int) + rfm['F_Score'].astype(int) + rfm['M_Score'].astype(int)

    # 4. Apply Business Logic Segments
    def assign_segment(score):
        if score >= 10:
            return 'VIP / Champions'
        elif score >= 6:
            return 'At Risk / Needs Attention'
        else:
            return 'Churned / Low Value'

    rfm['Customer_Segment'] = rfm['Total_Score'].apply(assign_segment)

    # 5. Export clean data for our PM Phase
    rfm.to_csv('analytics_engine/data/segmented_customers.csv')
    
    # Print out a mini data-summary to display in terminal
    print("\n====== MAROPS INSIGHT GENERATOR ======")
    print(rfm['Customer_Segment'].value_counts())
    print("=======================================")
    print("📊 Data exported to analytics_engine/data/segmented_customers.csv")

if __name__ == "__main__":
    run_rfm_analysis()
