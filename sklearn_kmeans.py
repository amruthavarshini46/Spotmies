import time
from sklearn.cluster import KMeans

def run_sklearn_kmeans(dataset, clusters=5):
    start_time = time.time()
    model = KMeans(n_clusters=clusters, n_init=10)
    predicted_labels = model.fit_predict(dataset)
    end_time = time.time()
    return predicted_labels, model.cluster_centers_, end_time - start_time
