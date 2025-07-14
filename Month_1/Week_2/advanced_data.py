ml_datasets = [
    ["Iris", "Boston Housing"],
    ["MNIST", "CIFAR-10"],
    ["IMDB Reviews", "Spam Detection"]
]

flattened = [dataset for group in ml_datasets for dataset in group]
print(flattened)