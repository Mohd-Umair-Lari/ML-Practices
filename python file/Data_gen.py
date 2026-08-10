import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def generate_mart_data(n_rows=1500):
    np.random.seed(42)
    
    data = {
        'basket_complexity_score': np.random.uniform(0, 10, n_rows),
        'perishability_index': np.random.uniform(0, 1, n_rows),
        'basket_value': np.random.exponential(scale=50, size=n_rows),
        'item_count': np.random.randint(1, 50, n_rows),
        'queue_wait_time': np.random.normal(5, 2, n_rows),
        'stock_out_flag': np.random.choice([0, 1], n_rows, p=[0.9, 0.1]),
        'discount_used': np.random.choice([0, 1], n_rows, p=[0.7, 0.3]),
        'distance_from_store': np.random.exponential(scale=5, size=n_rows),
        'customer_tenure_days': np.random.randint(0, 3650, n_rows),
        'past_visit_frequency': np.random.randint(0, 10, n_rows)
    }
    
    df = pd.DataFrame(data)
    
    score = (
        (df['perishability_index'] * 3) +       
        (df['past_visit_frequency'] * 0.5) -    
        (df['distance_from_store'] * 0.1) -     
        (df['basket_complexity_score'] * 0.05)
    )
    
    prob = 1 / (1 + np.exp(-(score - 1.5)))
    
    df['repeat'] = [1 if p > np.random.random() else 0 for p in prob]
    
    return df

df = generate_mart_data()
df.to_csv('mart_data.csv', index=False)
print("Data Shape:", df.shape) 