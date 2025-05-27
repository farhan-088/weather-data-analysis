def load_data(filepath):
    import pandas as pd
    df = pd.read_csv(filepath, parse_dates=['date'])
    return df

def handle_missing_values(df):
    df['temperature'].fillna(df['temperature'].mean(), inplace=True)
    df['precipitation'].fillna(0, inplace=True)
    return df

def clean_data(df):
    df.drop_duplicates(inplace=True)
    return df