"""Load the Iris dataset and upload it to Firebase and Supabase."""
import os
import pandas as pd
from dotenv import load_dotenv
from sklearn.datasets import load_iris

from firebase_client import upload_to_firebase
from supabase_client import upload_to_supabase


def load_iris_records():
    """Load the 150-row Iris dataset and convert it to JSON-compatible records."""
    iris = load_iris(as_frame=True)
    frame = iris.frame.rename(
        columns={
            "sepal length (cm)": "sepal_length",
            "sepal width (cm)": "sepal_width",
            "petal length (cm)": "petal_length",
            "petal width (cm)": "petal_width",
        }
    )
    frame["species"] = frame["target"].map(
        {index: name for index, name in enumerate(iris.target_names)}
    )
    frame.insert(0, "id", range(len(frame)))
    frame = frame.rename(columns={"target": "target"})
    records = frame[
        [
            "id", "sepal_length", "sepal_width", "petal_length",
            "petal_width", "target", "species"
        ]
    ].to_dict(orient="records")

    # Convert NumPy scalar values to native Python values for JSON clients.
    return [
        {
            key: (value.item() if hasattr(value, "item") else value)
            for key, value in record.items()
        }
        for record in records
    ]


def main():
    load_dotenv()
    records = load_iris_records()
    print(f"Loaded {len(records)} Iris records.")

    # Each destination is attempted independently so one failure does not
    # prevent the other database integration from being tested.
    for database_name, upload_function in (
        ("Firebase", upload_to_firebase),
        ("Supabase", upload_to_supabase),
    ):
        try:
            upload_function(records)
        except Exception as error:
            print(f"{database_name} upload failed: {error}")

    print("Integration run finished. Check the messages above for each result.")


if __name__ == "__main__":
    main()
