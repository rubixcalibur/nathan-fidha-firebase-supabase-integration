# Iris Dataset Integration with Firebase and Supabase

**Project:** Python API integration with two cloud databases  
**Dataset:** Iris flower dataset (150 records, 3 species)

## Overview
This project loads the Iris dataset, prepares consistent records, and uploads the same data to:
1. **Firebase Cloud Firestore** using the Firebase Admin Python SDK.
2. **Supabase** using the Supabase Python client and a PostgreSQL table.

The dataset is loaded from scikit-learn's built-in copy of the classic Iris dataset, so no manual download is needed.

## Project structure
```
.
├── main.py
├── firebase_client.py
├── supabase_client.py
├── schema.sql
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 1. Requirements
- Python 3.10+
- A Firebase project with Cloud Firestore enabled
- A Supabase project

Install dependencies:
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## 2. Configure Firebase
1. Open the Firebase console and create/select a project.
2. Create a Cloud Firestore database.
3. In Project settings → Service accounts, generate a private-key JSON file.
4. Store that JSON file locally in this project folder (or another secure location). Never commit it.
5. Set `FIREBASE_CREDENTIALS_PATH` in your local `.env` to its path.

## 3. Configure Supabase
1. Create a Supabase project.
2. Open the SQL Editor and run the contents of `schema.sql`.
3. In Project Settings → API, copy the Project URL and a server-side key.
4. Put them in your local `.env` as `SUPABASE_URL` and `SUPABASE_KEY`.

Use a server-side secret only in this trusted local script. Never expose it in browser code or commit it to GitHub. For a deployed app, use a restricted design and appropriate Row Level Security policies.

## 4. Set environment variables
Copy `.env.example` to `.env` and fill in your own values:
```bash
# Windows PowerShell
Copy-Item .env.example .env
# macOS/Linux
cp .env.example .env
```

## 5. Run
```bash
python main.py
```
The program loads 150 rows and uploads them to both cloud databases. Firestore documents use the dataset row index as a stable document ID; Supabase rows use `id` as the primary key, so rerunning the script updates the same logical records rather than creating duplicates.

## Database schema
The Supabase table is named `iris_flowers`. Its SQL definition is in `schema.sql`. Firestore uses a collection with the same name and one document per flower record.

## Dataset information
The Iris dataset contains four measurements (sepal length/width and petal length/width) and a species label for setosa, versicolor, or virginica. It is commonly distributed with scikit-learn. Dataset reference: Fisher, R. A. (1936), *The use of multiple measurements in taxonomic problems*.

## Security
- Do not upload `.env`, Firebase service-account JSON files, or API keys.
- Keep `.gitignore` enabled.
- If a key is accidentally published, revoke/rotate it immediately in the provider dashboard.

## Expected result
On successful execution, the terminal reports the number of records sent to Firestore and Supabase. You must configure your own Firebase and Supabase projects before running the upload; this repository does not contain cloud credentials.
