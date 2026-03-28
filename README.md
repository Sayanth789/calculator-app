# 🧮 Full Stack Scientific Calculator

A **full-stack scientific calculator application** built with **FastAPI**, **PostgreSQL**, and a **web frontend**.
The application provides powerful scientific calculations through a clean user interface and a high-performance backend API.

The entire system is **containerized using Docker and Docker Compose**, making it easy to run locally or deploy anywhere.

---

# ✨ Features

### 🧠 Scientific Calculator

Supports:

* Addition, subtraction, multiplication, division
* Exponentiation
* Square root
* Trigonometric functions (`sin`, `cos`, `tan`)
* Logarithmic calculations
* Complex mathematical expressions

---

### 🌐 Frontend Interface

* Interactive calculator UI
* Sends calculation requests to the backend API
* Displays results instantly
* Simple and responsive layout

---

### ⚡ FastAPI Backend

* High-performance Python API
* Handles mathematical expression evaluation
* Stores calculation history
* Automatic API documentation

---

### 💾 Database Support

* PostgreSQL database
* SQLAlchemy ORM
* Persistent calculation history storage

---

### 🐳 Dockerized Setup

The project includes:

* `Dockerfile`
* `docker-compose.yml`

You can run the **entire stack (frontend + API + database)** with a single command.

---

# 🛠 Tech Stack

**Backend**

* Python
* FastAPI
* Uvicorn
* SQLAlchemy
* psycopg2

**Database**

* PostgreSQL

**Frontend**

* HTML
* CSS
* JavaScript

**DevOps**

* Docker
* Docker Compose

---

# 📂 Project Structure

```
calculator-app
│
|
├── calculator.py
├── models.py
├── database.py
└── main.py
│
├── static
│   ├── index.html
│   
│__ tests
|   ├──test_calc.py
|
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 🚀 Running Locally

Clone the repository

```bash
git clone https://github.com/Sayanth789/calculator-app.git
cd calculator-app
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the API server

```bash
uvicorn main:app --reload
```

---

# 🐳 Running with Docker

Build the Docker image

```bash
docker build -t calculator-app .
```

Run the container

```bash
docker run -p 8000:8000 calculator-app
```

---

# 🐳 Running with Docker Compose

Start the full application stack:

```bash
docker-compose up --build
```

This will start:

* FastAPI backend
* PostgreSQL database
* Frontend interface

---

# 📖 API Documentation

FastAPI provides automatic interactive documentation.

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# 🧪 Example API Request

Request

```json
{
  "expression": "sin(30) + log(10)"
}
```

Response

```json
{
  "result": 2.5
}
```

---

# 🔮 Future Improvements

* Calculation history UI
* Graph plotting
* Authentication system
* Rate limiting
* Unit conversions
* Scientific constants

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve the project:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

# ⭐ Support

If you like this project, please **give it a star ⭐ on GitHub**.

It helps the project reach more developers and encourages further improvements.
