from sklearn.cluster import KMeans

def run_kmeans(df, cols):
    kmeans = KMeans(n_clusters=3, random_state=42)
    df["Customer_Cluster"] = kmeans.fit_predict(df[cols])

    print("Clustering Completed")
    print("\nCluster Count:")
    print(df["Customer_Cluster"].value_counts())

    return df