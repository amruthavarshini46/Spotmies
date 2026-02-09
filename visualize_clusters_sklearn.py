import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

print("Loading dataset...")
df = pd.read_csv("synthetic_online_communities_2025.csv")

# Use same numeric features
X = df[
    ["text_length", "toxicity_score", "engagement_score",
     "community_id", "age", "is_premium", "suspicious_score"]
]

print("Running KMeans for visualization...")
kmeans = KMeans(n_clusters=5, random_state=42)
labels = kmeans.fit_predict(X)

# Add labels to dataframe
df["cluster"] = labels

# 🔹 Sample for visualization (important!)
sample = df.sample(5000, random_state=42)

plt.figure(figsize=(7, 5))
plt.scatter(
    sample["text_length"],
    sample["engagement_score"],
    c=sample["cluster"],
    cmap="viridis",
    s=10
)

plt.xlabel("Text Length")
plt.ylabel("Engagement Score")
plt.title("Scikit-learn KMeans Cluster Visualization")
plt.colorbar(label="Cluster ID")
plt.show()
