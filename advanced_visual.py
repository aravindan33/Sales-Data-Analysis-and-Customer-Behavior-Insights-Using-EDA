import seaborn as sns
import matplotlib.pyplot as plt

def corr_heatmap(df):
    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(numeric_only=True),annot=True,cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()