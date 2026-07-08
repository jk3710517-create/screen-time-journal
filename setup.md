# Screen Time Journal - Setup Guide

## Project Overview

Screen Time Journal is a full-stack application developed to help users track and manage their daily screen usage. The backend is built using FastAPI and PostgreSQL, while the frontend communicates with the backend through REST APIs.

---

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- psycopg2
- Uvicorn
- Git & GitHub
- VS Code

---

## Project Structure

backend/
├── app.py
├── db.py
├── requirements.txt
├── setup.md
└── README.md

---

## Database Setup

1. Install PostgreSQL and pgAdmin.
2. Create a database named:

```
screen_time_journal
```

3. Execute the SQL scripts to create:
   - users
   - activities
   - screen_logs

4. Insert the sample data into all three tables.

---

## Configure Database Connection

Open `db.py` and update the following values according to your PostgreSQL installation:

- Host
- Database Name
- Username
- Password
- Port

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Backend

```bash
uvicorn app:app --reload
```

Server URL:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Features

- Database Connection
- User Management
- Activity Management
- Screen Log Management
- CRUD Operations
- REST APIs using FastAPI

---

## Developed By

**Jasleen Kaur**

B.Tech Computer Science Engineering (AI & Data Engineering)

Lovely Professional University