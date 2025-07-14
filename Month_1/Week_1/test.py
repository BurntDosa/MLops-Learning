import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from ml_utils import load_model
from sklearn.metrics import mean_squared_error
from sklearn.datasets import fetch_openml  # For sample data

# Load sample data (e.g., Boston housing)
data = fetch_openml(name='boston', version=1, as_frame=True)
X = data.data[['RM']]  # Use one feature for simplicity
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = load_model("LinearRegression")
model.fit(X_train, y_train)

# Predict and evaluate
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse:.2f}")
