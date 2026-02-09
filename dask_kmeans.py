import time
from dask_ml.cluster import KMeans

def run_dask_kmeans(dataset, clusters=5):
    model = KMeans(
        n_clusters=clusters,
        init_max_iter=5,
        max_iter=100
    )

    start_time = time.time()
    model.fit(dataset)
    end_time = time.time()

    return model.labels_, model.cluster_centers_, end_time - start_time
