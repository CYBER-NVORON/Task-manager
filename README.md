# Task Manager (Flask)

A simple and extensible Task Manager built with Python and Flask.  
The project includes user registration, authentication, data isolation, and basic CRUD operations for tasks.

---

## Features

- User registration and authentication
- Secure password hashing
- Separate task lists for each user
- Create, edit, delete tasks
- Mark tasks as completed
- Route protection using Flask-Login
- SQLite database via SQLAlchemy
- Environment variables stored in `.env`
- Docker and Docker Compose support

---

## Technology Stack

- Python 3.10+
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Werkzeug (password hashing)
- SQLite
- Bootstrap (frontend)
- Docker / Docker Compose
- python-dotenv

---

## Environment Variables

Create a `.env` file in the project root:

```env
FLASK_ENV=development
FLASK_DEBUG=1

SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///tasks.db
```

The `.env` file must not be committed to the repository.

---

## Running Without Docker

### 1. Clone the repository

```bash
git clone https://github.com/your-username/task-manager.git
cd Task-manager
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### Activate it

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a .env file

```
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
```
### 5. Run the application

```bash
python app.py
```

The application will be available at:

```
http://localhost:5000
```

## Running with Docker
### 1. Build and start containers

```bash
docker compose up --build
```

### 2. Open in browser

```bash
http://localhost:5000
```

## License

This project is created for educational purposes and can be freely used and modified.