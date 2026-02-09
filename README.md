**Scalable K-Means Clustering using Dask**

# Project Overview :
This project explains how k-means clustering can be used with large amounts of data by using Dask.
Normally, k-means runs on a single machine, which can be slow or difficult when the dataset becomes very large.
Dask helps solve this problem by allowing the computation to run in parallel, using multiple CPU cores or even multiple machines.

In this project, k-means clustering is implemented using both scikit-learn and Dask.
The performance of both methods is compared to understand how Dask improves scalability and execution speed when working with larger datasets.

The project also includes a visualization of the clusters so that the clustering results can be easily understood.

To make the project simple to run and easy to share, the dataset is generated automatically when the program runs.
This means no large data files are needed, and anyone can run the project on their own system without extra setup.

# Objectives :
1. Implement scalable k-means clustering using Dask.
2. Generate a synthetic dataset with a large number of samples.
3. Compare execution time with scikit-learn k-means.
4. Visualize cluster assignments clearly.
5. Support both local and cluster-based execution.

# Technologies Used :   
1. Python
2. Dask & Dask-ML for parallel computation
3. scikit-learn for baseline comparison
4. NumPy and Pandas for data handling
5. Matplotlib for visualization

# Project Structure :

├── data_generation.py                # Generates synthetic dataset
├── sklearn_kmeans.py                 # scikit-learn k-means implementation
├── dask_kmeans.py                    # Dask-based k-means implementation
├── Performance_benchmark.py          # Performance comparison script
├── visualize.py                      # Cluster visualization
├── run_local.py                      # Local execution using Dask
├── run_cluster.py                    # Cluster-aware execution
└── README.md

# Setup Instructions
Step 1: Create a virtual environment
  i havent
   
