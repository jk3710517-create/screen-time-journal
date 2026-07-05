# Screen Time Journal API

## Project Description

The Screen Time Journal API is a backend project developed using FastAPI and PostgreSQL. It helps users manage and track their daily screen time activities. The API supports viewing, adding, updating, and deleting screen log records.

---

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- psycopg2
- Pydantic
- Uvicorn

---

## Features

- View all users
- View all activities
- View all screen logs
- Add a new screen log
- Update screen log hours
- Delete a screen log

---

## Project Structure

```
backend/
│── app.py
│── db.py
│── requirements.txt
│── README.md
```

---

## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the server:

```bash
uvicorn app:app --reload
```

---

## API Endpoints

| Method | Endpoint |
|---------|----------|
| GET | / |
| GET | /users |
| GET | /activities |
| GET | /screenlogs |
| POST | /screenlogs |
| PUT | /screenlogs/{log_id} |
| DELETE | /screenlogs/{log_id} |

---

## Author

Jasleen Kaur
