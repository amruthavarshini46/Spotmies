import pandas as pd

# Load dataset
df = pd.read_csv("synthetic_online_communities_2025.csv")

print("Dataset shape:", df.shape)
print("\nColumn types:\n", df.dtypes)
print("\nFirst 5 rows:\n", df.head())
