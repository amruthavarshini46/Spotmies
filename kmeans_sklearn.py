import pandas as pd
import time
from sklearn.cluster import KMeans

print("Loading dataset...")
df = pd.read_csv("synthetic_online_communities_2025.csv")

# Select numeric features (same as you used)
X = df[
    ["text_length", "toxicity_score", "engagement_score",
     "community_id", "age", "is_premium", "suspicious_score"]
]

print("Running Scikit-learn KMeans...")
start = time.time()

kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(X)

sk_time = time.time() - start
print(f"Scikit-learn Time: {sk_time:.2f} seconds")

# ✅ Save time to file
with open("sklearn_time.txt", "w") as f:
    f.write(str(sk_time))
