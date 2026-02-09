import dask.array as da

def generate_dataset(
    total_samples=500_000,
    total_features=2,
    chunk_size=100_000
):
    dataset = da.random.random(
        size=(total_samples, total_features),
        chunks=(chunk_size, total_features)
    )
    return dataset

if __name__ == "__main__":
    data = generate_dataset()
    print(data)
