from sklearn.preprocessing import StandardScaler

def transform_data(df, num_cols):
    scaler = StandardScaler()

    print("\nBefore Scaling:")
    print(df[num_cols].head())

    df[num_cols] = scaler.fit_transform(df[num_cols].values)

    print("\nAfter Scaling:")
    print(df[num_cols].head())

    print("Data Transformation Done")
    return df
