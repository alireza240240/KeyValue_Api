# 🔑 Key-Value Management API
A complete project for managing **key/value** pairs using **Django REST Framework** and **JWT Authentication**.

---

## 🚀 Features
- JWT-based authentication
- Add, view, and update key/value pairs
- Retrieve a list of all key/value pairs
- PostgreSQL database integration
- Automatic API documentation using Swagger (OpenAPI)
- Fully containerized with Docker and Docker Compose

---

## 🛠️ Technologies
- **Python 3.13**
- **Django 5**
- **Django REST Framework**
- **Simple JWT**
- **PostgreSQL**
- **drf-yasg** (Swagger)
- **Docker / Docker Compose**

---

## ⚙️ Requirements
Before running the project, make sure you have the following installed:
- [Python 3.10+](https://www.python.org/downloads/)
- [Docker & Docker Compose](https://www.docker.com/)

---

## 📦 Installation & Run

### 🐳 Run with Docker (recommended)

```bash
docker compose up --build
```

Then open your browser at:
👉 http://127.0.0.1:8000/swagger/

All services (PostgreSQL & Django) will start automatically.

---

### 🧰 Run manually (without Docker)

```bash
python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

---

## 🔐 JWT Authentication

| Method | Endpoint | Description |
|--------|-----------|-------------|
| `POST` | `/auth/login/` | Obtain access and refresh tokens |
| `POST` | `/auth/refresh/` | Refresh access token |

**Example request:**
```json
POST /auth/login/
{
  "username": "testuser",
  "password": "test1234"
}
```

---

## 🔑 Key/Value Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| `GET` | `/api/kv/` | Retrieve all key/value pairs |
| `POST` | `/api/kv/` | Create a new key/value pair |
| `GET` | `/api/kv/{key}/` | Get a specific value by key |
| `PUT` | `/api/kv/{key}/` | Create or update a specific key |

---

## 🗂️ Project Structure

```
kv_api_project/
├── kv_api/               # Main project configuration
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── kvmanage/             # Main app (KeyValue API)
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── ...
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── .env
└── README.md
```

---

## 👤 Author
- **Name:** [AlirezaKhosravi]
- **Email:** [khosravialireza2424@gmail.com]

---

## 🏁 Note
This project was developed as part of an internship technical task.
It includes all required components: JWT Authentication, CRUD operations, PostgreSQL, OpenAPI documentation, and Docker containerization.
