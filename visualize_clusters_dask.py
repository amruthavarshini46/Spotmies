import dask.dataframe as dd
import matplotlib.pyplot as plt
from dask_ml.cluster import KMeans

print("Loading dataset with Dask...")
ddf = dd.read_csv("synthetic_online_communities_2025.csv")

X = ddf[
    ["text_length", "toxicity_score", "engagement_score",
     "community_id", "age", "is_premium", "suspicious_score"]
]

print("Running Dask KMeans...")
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(X)

labels = kmeans.predict(X)

# Convert to Pandas for plotting
plot_df = ddf.assign(cluster=labels).sample(frac=0.005).compute()

plt.figure(figsize=(7, 5))
plt.scatter(
    plot_df["text_length"],
    plot_df["engagement_score"],
    c=plot_df["cluster"],
    cmap="plasma",
    s=10
)

plt.xlabel("Text Length")
plt.ylabel("Engagement Score")
plt.title("Dask KMeans Cluster Visualization")
plt.colorbar(label="Cluster ID")
plt.show()
