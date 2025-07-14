# Nested Lists and flattening
ml_datasets = [
    ["Iris", "Boston Housing"],
    ["MNIST", "CIFAR-10"],
    ["IMDB Reviews", "Spam Detection"]
]

flattened = [dataset for group in ml_datasets for dataset in group]
#print(flattened)

model_config = {
    'model_type': 'regression',
    'params': {
        'learning_rate': 0.01,
        'epochs' : 100
    },
    'features': ['age', 'income']
}

model = input("Choose the model you want to use: ")
print(model)

if model == "Linear Regression":
    model_config['model_type'] = model
    model_config['params']['learning_rate'] = 0.005
else:
    model_config['params']['learning_rate'] = 0.1

model_config['optimised_for'] = 'Mac ARM'
print(model_config)