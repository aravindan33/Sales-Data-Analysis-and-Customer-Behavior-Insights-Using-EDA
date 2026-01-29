import seaborn as sns
import matplotlib.pyplot as plt

def probability_dist(df, col):
    sns.kdeplot(df[col], fill=True)
    plt.title(f"Probability Distribution of {col}")
    plt.show()