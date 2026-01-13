# NotesVault API

NotesVault is a small backend service that allows users to register, log in, and manage private notes through a REST API.  
Each user can only access their own notes.

The project is designed as a **portfolio example** demonstrating modern backend and DevOps fundamentals.

---

## Features

- User registration and login
- JWT-based authentication
- Protected endpoints
- User-scoped data access
- SQLite persistence
- Dockerized setup
- Interactive API documentation (Swagger)

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT (OAuth2 password flow)
- Docker

---

## Running locally with Docker

### Prerequisites
- Docker installed and running

### Build the image
```bash
docker build -t notesvault-api .
