def add_features(df):
    df['temperature_range'] = df['max_temp'] - df['min_temp']
    df['is_rainy_day'] = df['precipitation'] > 0
    return df