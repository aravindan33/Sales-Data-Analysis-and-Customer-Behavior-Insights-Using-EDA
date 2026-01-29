def descriptive_statistics(df):
    print("\nDescriptive Statistics:")
    print(df.describe())

    print("\nMean Values:")
    print(df.mean(numeric_only=True))