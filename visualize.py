import matplotlib.pyplot as plt

# ✅ Read times from files (PATH-BASED)
with open("sklearn_time.txt", "r") as f:
    sk_time = float(f.read())

with open("dask_time.txt", "r") as f:
    dask_time = float(f.read())

methods = ["Scikit-learn", "Dask"]
times = [sk_time, dask_time]

plt.figure(figsize=(6, 4))
plt.bar(methods, times)
plt.ylabel("Execution Time (seconds)")
plt.title("K-Means Performance Comparison")

# Add labels
for i, v in enumerate(times):
    plt.text(i, v, f"{v:.2f}s", ha="center", va="bottom")

plt.show()
