
---

# Scalable K-Means Clustering using Dask

# 1. Project Overview

> This project shows how k-means clustering can be applied to large datasets using Dask. Normally, k-means runs on a single machine, which can become slow or inefficient as the dataset size increases. Dask addresses this limitation by enabling parallel computation across multiple CPU cores or machines, improving performance for large-scale data processing.
>
> In this project, k-means clustering is implemented using both scikit-learn and Dask, and their performance is compared to highlight the scalability benefits of Dask. The project also includes visualizations of the clusters to make the results easy to understand.
>
> To keep the project simple and easy to run, the dataset is generated automatically at runtime. This removes the need for large data files and allows anyone to run the project on their system without additional setup.


---

# 2. Objectives

* Implement scalable k-means clustering using Dask
* Generate a synthetic dataset with a large number of samples
* Compare execution time with scikit-learn k-means
* Visualize cluster assignments clearly
* Support both local and cluster-based execution

---

# 3. Technologies Used

* Python
* Dask & Dask-ML (parallel computation)
* scikit-learn (baseline comparison)
* NumPy and Pandas (data handling)
* Matplotlib (visualization)

---

# 4. Project Structure

```text

├── data_generation.py        # Generates synthetic dataset
├── sklearn_kmeans.py         # scikit-learn k-means implementation
├── dask_kmeans.py            # Dask-based k-means implementation
├── benchmark.py              # Performance comparison script
├── visualize.py              # Cluster visualization
├── run_local.py              # Local execution using Dask
├── run_cluster.py            # Cluster-aware execution
└── README.md                 # Project documentation
```

---

# 5. Setup Instructions

## Step 1: Create a virtual environment

```bash
python -m venv .venv
```

## Step 2: Activate the environment

**Windows (PowerShell)**

```bash
.venv\Scripts\Activate.ps1
```

## Step 3: Install dependencies

```bash
pip install dask[complete] dask-ml scikit-learn numpy pandas matplotlib
```

---

# 6. Data Generation

The dataset is generated programmatically using **Dask arrays** with:

* 500,000 samples
* 2 features
* Chunked execution for parallel processing

This approach avoids storing large data files and ensures reproducibility on any system.

---

# 7. How to Run the Project

## 1. Run Locally

Runs Dask on the local machine using available CPU cores.

```bash
python run_local.py
```

This will:

* Start a local Dask client
* Generate the dataset
* Perform k-means clustering using Dask
* Display the cluster visualization

---

## 2. Performance Benchmark

Compares execution time of **scikit-learn k-means** and **Dask k-means** on the same dataset.

```bash
python benchmark.py
```

The output shows execution time for both approaches in tabular form and a comparison graph.

---

## 3. Run on a Dask Cluster (Optional)

This script attempts to connect to a Dask cluster.
If no cluster is available, it automatically falls back to local execution.

```bash
python run_cluster.py
```

---

# 8. Visualization

Cluster results are visualized using **Matplotlib**.

* X-axis: Feature 1
* Y-axis: Feature 2
* Cluster centers are highlighted for better interpretation

To maintain clarity, only a subset of the dataset is plotted.

---

# 9. Results and Observations

* scikit-learn performs well on smaller datasets
* Dask enables parallel execution and scalability
* Dask can handle larger datasets that may not fit comfortably in memory using traditional approaches

---

# 10. Key Notes

* No raw dataset files are included
* Data is generated dynamically at runtime
* Code is modular and easy to extend
* Supports both local and cluster execution

---

# 11. Conclusion

> This project demonstrates how Dask can be used to scale traditional machine learning algorithms such as k-means clustering. By using parallel and distributed computing, Dask allows the algorithm to efficiently process large datasets that may be slow or difficult to handle on a single machine.
>
> The project highlights how Dask improves performance and scalability while keeping the code clean, reusable, and easy to understand. It also shows how distributed execution can be applied without changing the core logic of the algorithm, making it practical for real-world data processing tasks. Overall, this project illustrates how Dask enables efficient and reproducible machine learning workflows for large-scale data.


---

