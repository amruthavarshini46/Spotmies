import numpy as np
import pandas as pd
import dask.array as da
import matplotlib.pyplot as plt

from sklearn_kmeans import run_sklearn_kmeans
from dask_kmeans import run_dask_kmeans

def benchmark_execution():
    results = []

    total_samples = 500_000
    total_features = 2

    dataset_numpy = np.random.random((total_samples, total_features))

    _, _, sklearn_time = run_sklearn_kmeans(dataset_numpy)
    results.append(["Scikit-learn", total_samples, sklearn_time])

    dataset_dask = da.from_array(dataset_numpy, chunks=(100_000, total_features))
    _, _, dask_time = run_dask_kmeans(dataset_dask)
    results.append(["Dask", total_samples, dask_time])

    result_table = pd.DataFrame(
        results,
        columns=["Method", "Samples", "Execution Time (seconds)"]
    )

    print(result_table)

    plot_performance(result_table)

def plot_performance(result_table):
    plt.figure(figsize=(6, 4))
    plt.bar(
        result_table["Method"],
        result_table["Execution Time (seconds)"]
    )

    plt.xlabel("Method", fontweight="bold", fontsize=12)
    plt.ylabel("Execution Time (seconds)", fontweight="bold", fontsize=12)
    plt.title("K-Means Performance Comparison", fontweight="bold", fontsize=13)

    plt.xticks(fontweight="bold")
    plt.yticks(fontweight="bold")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    benchmark_execution()
