from dask.distributed import Client
from data_generation import generate_dataset
from dask_kmeans import run_dask_kmeans

if __name__ == "__main__":
    try:
        client = Client("tcp://127.0.0.1:8786")
        print("Connected to Dask cluster")
    except Exception:
        client = Client()
        print("No cluster found, running locally")

    dataset = generate_dataset()
    labels, centers, execution_time = run_dask_kmeans(dataset)

    print(f"Execution time: {execution_time:.2f} seconds")
