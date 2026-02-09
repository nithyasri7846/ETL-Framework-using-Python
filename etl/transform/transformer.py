import pandas as pd

def transform(df):
    df["processed_at"] = pd.Timestamp.now()
    return df
