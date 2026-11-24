"""Firebase Cloud Firestore upload functions."""
import os
import firebase_admin
from firebase_admin import credentials, firestore


def get_firestore_client():
    """Initialize Firebase once and return a Firestore client."""
    if not firebase_admin._apps:
        credentials_path = os.getenv("FIREBASE_CREDENTIALS_PATH")
        if not credentials_path:
            raise ValueError("FIREBASE_CREDENTIALS_PATH is missing from .env")
        if not os.path.isfile(credentials_path):
            raise FileNotFoundError(
                f"Firebase credentials file not found: {credentials_path}"
            )
        cred = credentials.Certificate(credentials_path)
        firebase_admin.initialize_app(cred)
    return firestore.client()


def upload_to_firebase(records):
    """Upload records to the iris_flowers collection using stable document IDs."""
    db = get_firestore_client()
    collection = db.collection("iris_flowers")

    # Firestore batches support up to 500 writes. 150 Iris rows fit in one batch.
    batch = db.batch()
    for record in records:
        document_id = str(record["id"])
        batch.set(collection.document(document_id), record)
    batch.commit()
    print(f"Firebase Firestore: uploaded {len(records)} records.")
