# Dataset

The project loads the 150-row Iris dataset from scikit-learn at runtime using `sklearn.datasets.load_iris`. This avoids duplicating the dataset file and makes setup reproducible. The four numeric features and species label are converted to records in `main.py`.
