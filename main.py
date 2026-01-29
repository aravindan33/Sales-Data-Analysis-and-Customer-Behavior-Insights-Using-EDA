from data_loader import load_data
from data_cleaner import clean_data
from data_transform import transform_data
from descriptive_stats import descriptive_statistics
from basic_visual import plot_hist
from advanced_visual import corr_heatmap
from interactive_visual import interactive_plot
from probability_analysis import probability_dist
from kmeans_cluster import run_kmeans
from data_export import export_data
from summary_report import summary

# Load dataset
df = load_data("retail_sales_dataset.csv")

# Clean data
df = clean_data(df)

# Select numeric columns
num_cols = df.select_dtypes(include=["int64", "float64"]).columns

# Transform data
df = transform_data(df, num_cols)

# Analysis & Visualization
descriptive_statistics(df)
plot_hist(df)
corr_heatmap(df)
interactive_plot(df, num_cols[0], num_cols[1])
probability_dist(df, num_cols[0])

# Clustering
df = run_kmeans(df, num_cols)

# Export & Summary
export_data(df)
summary()