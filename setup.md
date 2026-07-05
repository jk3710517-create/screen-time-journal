# Screen Time Journal API - Setup Guide

## Prerequisites

Before running the project, make sure you have installed:

- Python 3.10 or later
- PostgreSQL
- Git
- Visual Studio Code

---

## Step 1: Clone the Repository

```bash
git clone <repository-url>
```

Open the project folder:

```bash
cd screen-time-journal
```

---

## Step 2: Create a Virtual Environment

Go to the backend folder:

```bash
cd backend
```

Create the virtual environment:

```bash
python -m venv venv
```

Activate it (Windows):

```bash
.\venv\Scripts\activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Configure PostgreSQL

1. Open PostgreSQL.
2. Create the required database.
3. Update the database connection details in `db.py`:

- Host
- Database Name
- Username
- Password

---

## Step 5: Run the FastAPI Server

```bash
uvicorn app:app --reload
```

---

## Step 6: Open the API Documentation

Open your browser and visit:

```
http://127.0.0.1:8000/docs
```

---

## Available APIs

- GET /
- GET /users
- GET /activities
- GET /screenlogs
- POST /screenlogs
- PUT /screenlogs/{log_id}
- DELETE /screenlogs/{log_id}

---

## Project Developed By

Jasleen Kaur