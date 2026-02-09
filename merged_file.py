import pandas as pd

# Load dataset
df = pd.read_csv("synthetic_online_communities_2025.csv")

# Select meaningful numeric columns
features = [
    "text_length",
    "toxicity_score",
    "engagement_score",
    "age",
    "is_premium",
    "suspicious_score",
    "community_id"
]

X = df[features]

print("Selected feature shape:", X.shape)
