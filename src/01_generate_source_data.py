import pandas as pd
import numpy as np
import uuid
from datetime import datetime, timedelta
import os
from config.config import *


def generate_transactions(batch_size):
    """Generate a DataFrame of random transactions"""
    # Create date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    random_dates = pd.to_datetime([
        start_date + (end_date - start_date) * np.random.random()
        for _ in range(batch_size)
    ])

    # Create DataFrame
    df = pd.DataFrame({
        'transaction_id': [str(uuid.uuid4()) for _ in range(batch_size)],
        'customer_id': [str(uuid.uuid4()) for _ in range(batch_size)],
        'transaction_date': random_dates,
        'amount': np.round(np.random.uniform(5, 500, batch_size), 2),
        'product_category': np.random.choice(
            ['Electronics', 'Clothing', 'Groceries', 'Home', 'Books'],
            batch_size
        ),
        'payment_method': np.random.choice(
            ['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer'],
            batch_size
        )
    })

    return df


def save_to_csv(df, filename=None):
    """Save DataFrame to CSV"""
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"transactions_{timestamp}.csv"

    os.makedirs("data", exist_ok=True)
    filepath = os.path.join("data", filename)

    df.to_csv(filepath, index=False)
    print(f"Saved {len(df)} records to {filepath}")
    return filepath


if __name__ == "__main__":
    # Generate and save data
    batch_size = np.random.randint(int(BATCH_SIZE_MIN), int(BATCH_SIZE_MAX) + 1)
    transactions = generate_transactions(batch_size)
    save_to_csv(transactions)

