**Scalable K-Means Clustering using Dask**

# 1. Project Overview :
This project explains how k-means clustering can be used with large amounts of data by using Dask.
Normally, k-means runs on a single machine, which can be slow or difficult when the dataset becomes very large.
Dask helps solve this problem by allowing the computation to run in parallel, using multiple CPU cores or even multiple machines.

In this project, k-means clustering is implemented using both scikit-learn and Dask.
The performance of both methods is compared to understand how Dask improves scalability and execution speed when working with larger datasets.

The project also includes a visualization of the clusters so that the clustering results can be easily understood.

To make the project simple to run and easy to share, the dataset is generated automatically when the program runs.
This means no large data files are needed, and anyone can run the project on their own system without extra setup.

# 2. Objectives :
1. Implement scalable k-means clustering using Dask.
2. Generate a synthetic dataset with a large number of samples.
3. Compare execution time with scikit-learn k-means.
4. Visualize cluster assignments clearly.
5. Support both local and cluster-based execution.

# 3. Technologies Used :   
1. Python
2. Dask & Dask-ML for parallel computation
3. scikit-learn for baseline comparison
4. NumPy and Pandas for data handling
5. Matplotlib for visualization


# 4. Project Structure
```

├── data_generation.py        # Generates synthetic dataset
├── sklearn_kmeans.py         # scikit-learn k-means implementation
├── dask_kmeans.py            # Dask-based k-means implementation
├── Performance_benchmark.py  # Performance comparison script
├── visualize.py              # Cluster visualization
├── run_local.py              # Local execution using Dask
├── run_cluster.py            # Cluster-aware execution
└── README.md                 # Project documentation
```
# 5. Setup Instructions :
Step 1: Create virtual environment
``` bash 
python -m venv .venv
```
Step 2: Activate virtual environment
``` bash 
.venv\Scripts\Activate.ps1
```
Step 3: Install dependencies
``` bash
pip install dask[complete] dask-ml scikit-learn numpy pandas matplotlib
```
# 6. How Data is Generated 
The dataset is generated using Dask arrays with:

* 500,000 samples

* 2 features

* Chunked execution for parallel processing

No dataset files are stored.

# 7. Running the Project


