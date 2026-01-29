import matplotlib.pyplot as plt

def plot_hist(df):
    df.hist(figsize=(10,6))
    plt.suptitle("Sales Data Distribution")
    plt.show()