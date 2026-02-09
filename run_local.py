from dask.distributed import Client

from data_generation import generate_dataset
from dask_kmeans import run_dask_kmeans
from visualize import plot_clusters

if __name__ == "__main__":
    Client()

    dataset = generate_dataset()
    labels, centers, _ = run_dask_kmeans(dataset)

    plot_clusters(
        dataset[:200_000],
        labels[:200_000],
        centers
    )
