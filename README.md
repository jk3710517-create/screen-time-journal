# 📱 Screen Time Journal

A Full Stack Screen Time Tracking application developed using **FastAPI**, **PostgreSQL**, and **Python**. The project helps users record, manage, and analyze their daily screen usage across different devices and activities.

---

## 🚀 Project Overview

Screen Time Journal allows users to:

- Register and manage users
- Store different activities (Coding, YouTube, Netflix, Reading, etc.)
- Record daily screen time
- Track device usage
- Perform complete CRUD operations
- Store all data in PostgreSQL

---

## ✨ Features

- User Management
- Activity Management
- Screen Time Logging
- Create, Read, Update & Delete (CRUD)
- FastAPI REST APIs
- PostgreSQL Database Integration

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- PostgreSQL
- psycopg2
- Uvicorn

### Tools
- VS Code
- pgAdmin
- Git
- GitHub

---

## 📂 Project Structure

```text
screen-time-journal/
│
├── backend/
│   ├── app.py
│   ├── db.py
│   ├── requirements.txt
│   ├── setup.md
│   └── README.md
```

---

## 🗄️ Database Tables

### Users
- user_id
- name
- email
- password
- created_at

### Activities
- activity_id
- activity_name
- category

### Screen Logs
- log_id
- user_id
- activity_id
- log_date
- device
- hours_spent

---

## 🔄 CRUD Operations

- Create Screen Log
- View Users
- View Activities
- View Screen Logs
- Update Screen Log
- Delete Screen Log

---

## ▶️ Running the Project

```bash
uvicorn app:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🎯 Future Enhancements

- User Authentication
- Dashboard with Charts
- Weekly & Monthly Reports
- Mobile Responsive Frontend
- AI-based Screen Time Analysis

---

## 👩‍💻 Developed By

**Jasleen Kaur**

B.Tech Computer Science Engineering (AI & Data Engineering)

Lovely Professional University

---

⭐ Thank you for visiting this repository!