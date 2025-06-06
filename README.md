
# 📲 Social Media Posts API (FastAPI)

A full-featured backend API for a simple social media-style platform, built using **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. It supports user authentication, post creation, and voting functionality — all with clean, modular architecture and JWT-based security.

---

## 🚀 Features

- 🔐 **JWT Authentication** with OAuth2
- 🧑 **User registration and login**
- 📝 **CRUD operations** for posts
- 👍 **Voting system** (upvote/downvote posts)
- 🧩 **SQLAlchemy ORM** with Alembic migrations
- 📃 **Swagger/OpenAPI** docs at `/docs`
- 🌱 Modular codebase using FastAPI routers and dependencies

---

## 🛠️ Tech Stack

- **FastAPI** - Web framework
- **PostgreSQL** - Relational database
- **SQLAlchemy** - ORM
- **Alembic** - Migrations
- **Passlib** - Password hashing
- **PyJWT** - JWT token handling
- **Uvicorn** - ASGI server

---

## 📁 Project Structure

```
socialmediaPosts_fastapi/
├── app/
│   ├── main.py                # Entry point
│   ├── models.py              # SQLAlchemy models
│   ├── schemas.py             # Pydantic schemas
│   ├── database.py            # DB connection
│   ├── oauth2.py              # JWT and auth utilities
│   ├── utils.py               # Helper functions (e.g. hashing)
│   └── routers/
│       ├── post.py            # Post-related routes
│       ├── user.py            # User-related routes
│       ├── auth.py            # Login/auth routes
│       └── vote.py            # Voting endpoints
├── alembic/                   # DB migrations
├── .env                       # Environment variables (not tracked)
├── requirements.txt           # Python dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/rutvijmavani/socialmediaPosts_fastapi.git
cd socialmediaPosts_fastapi
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix/macOS:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## ▶️ Running the App

### Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Visit the interactive API docs at:  
🔗 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔄 Alembic Migrations

To initialize and apply database migrations:

```bash
alembic init alembic
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

---

## 🧪 Example Endpoints

| Method | Endpoint          | Description                |
|--------|-------------------|----------------------------|
| POST   | `/users/`         | Register a new user        |
| POST   | `/login/`         | Log in and get JWT token   |
| GET    | `/posts/`         | Get all posts              |
| POST   | `/posts/`         | Create a new post          |
| POST   | `/vote/`          | Upvote or remove vote      |

---


## 📌 Notes

- Make sure PostgreSQL is running and accessible with the credentials from your `.env`.
- Don't forget to include `.env` in your `.gitignore` file to protect your secrets.
