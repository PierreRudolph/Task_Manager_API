# Task Manager API

A secure and modular RESTful Task Manager built with **Flask**, **SQLite**, and **JWT Authentication**.

This project provides user registration/login, protected task management, and full CRUD functionality with scalable architecture using Blueprints and Extensions.

---

## Features

### User Authentication
- User Registration
- User Login
- JWT Access Token Authentication
- Password Hashing (`werkzeug.security`)
- Protected Routes

### Task Management
- Create Tasks
- View All Personal Tasks
- View Single Task by ID
- Update Existing Tasks
- Delete Tasks
- Task Ownership Validation

### Security
- JWT Authentication
- Password Hashing + Salt
- Environment Variables (`.env`)
- Rate Limiting
- Input Validation
- CORS Configuration
- Blueprint-based Modular Structure

---

## Tech Stack

- **Backend:** Flask
- **Database:** SQLite
- **ORM:** Flask-SQLAlchemy
- **Authentication:** Flask-JWT-Extended
- **Security:** Werkzeug Password Hashing
- **Rate Limiting:** Flask-Limiter
- **Environment Config:** python-dotenv

---

## Project Structure

```plaintext
task-manager-api/
│── app.py
│── extensions.py
│── models.py
│── requirements.txt
│── .env.example
│── .gitignore
│
├── routes/
│   ├── auth.py
│   └── tasks.py
