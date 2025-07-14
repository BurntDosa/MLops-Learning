import numpy as np

def load_model(model_name):
    match model_name:
        case "LogisticRegression":
            from sklearn.linear_model import LogisticRegression
            return LogisticRegression()
        case "RandomForestClassifier":
            from sklearn.ensemble import RandomForestClassifier
            return RandomForestClassifier()
        case "SVC":
            from sklearn.svm import SVC
            return SVC()
        case "LinearRegression":
            from sklearn.linear_model import LinearRegression
            return LinearRegression()
        case "KMeans":
            from sklearn.cluster import KMeans
            return KMeans()
        case _:
            raise ValueError(f"Model {model_name} not recognized.")
