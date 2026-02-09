import matplotlib.pyplot as plt

def plot_clusters(dataset, labels, centers):
    dataset = dataset.compute() if hasattr(dataset, "compute") else dataset

    plt.figure(figsize=(7, 7))
    plt.scatter(dataset[:, 0], dataset[:, 1], c=labels, s=1, cmap="viridis")
    plt.scatter(centers[:, 0], centers[:, 1], c="black", s=200, marker="X")

    plt.xlabel("Feature 1", fontweight="bold", fontsize=13)
    plt.ylabel("Feature 2", fontweight="bold", fontsize=13)
    plt.title("Visualization of Clusters", fontweight="bold", fontsize=14)

    plt.show()
