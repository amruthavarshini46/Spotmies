import time
import dask.dataframe as dd
from dask_ml.cluster import KMeans
from dask.distributed import Client

client = Client(processes=False)  # faster for single machine

print("Loading dataset with Dask...")
ddf = dd.read_csv("synthetic_online_communities_2025.csv")

X = ddf[
    ["text_length", "toxicity_score", "engagement_score",
     "community_id", "age", "is_premium", "suspicious_score"]
]

print("Running Dask KMeans...")
start = time.time()

kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(X)

dask_time = time.time() - start
print(f"Dask Time: {dask_time:.2f} seconds")

# ✅ Save time to file
with open("dask_time.txt", "w") as f:
    f.write(str(dask_time))

client.close()
