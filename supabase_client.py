"""Supabase PostgreSQL upload functions."""
import os
from supabase import create_client


def upload_to_supabase(records):
    """Upsert records into public.iris_flowers using id as the conflict key."""
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    if not url or not key:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in .env")

    client = create_client(url, key)
    response = client.table("iris_flowers").upsert(
        records, on_conflict="id"
    ).execute()

    print(f"Supabase: upload request completed for {len(records)} records.")
    return response
