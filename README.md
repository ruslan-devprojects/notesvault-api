# NotesVault API

NotesVault is a small full-stack application that allows users to register, log in, and manage private notes.  
Each user can only access their own notes via secure authentication.

This project is built as a **portfolio-quality backend + frontend system**, focusing on real-world engineering practices rather than UI polish.

---

## Live Demo

- Backend API: https://notesvault-api.onrender.com
- API Docs (Swagger): https://notesvault-api.onrender.com/docs
- Frontend (local): http://localhost:5173

---

## Features

- User registration and login
- JWT-based authentication (OAuth2 password flow)
- Protected API endpoints
- User-scoped note access
- Persistent storage with PostgreSQL
- Health check endpoints
- Dockerized backend
- Cloud deployment (Render + Neon)
- Simple React frontend

---

## Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL (Neon)
- JWT authentication
- Docker
- Uvicorn

### Frontend
- React
- Vite
- Fetch API
- LocalStorage for auth token

### Infrastructure
- Render (API hosting)
- Neon (PostgreSQL)
- GitHub (source control)

---

## Architecture Overview

- The backend is **stateless**
- Authentication is handled using **JWT bearer tokens**
- User identity is resolved on every request via dependency injection
- All persistent data is stored in **PostgreSQL**
- Secrets are injected via **environment variables**
- A `/healthz` endpoint is included for cloud health checks
- Frontend communicates with the API over HTTPS

---

## Running the Backend Locally (Docker)

### Prerequisites
- Docker installed and running

### Build the image
```bash
docker build -t notesvault-api .


Runnning the container

docker run -p 8000:8000 notesvault-api

The API will be available at:
	•	http://127.0.0.1:8000/healthz
	•	http://127.0.0.1:8000/docs

Note: When running locally without an external database, the app uses SQLite by default.

⸻

Running the Frontend Locally

cd notesvault-web
npm install
npm run dev

Frontend will be available at:
	•	http://localhost:5173

⸻

Environment Variables (Backend)

Variable Description
DATABASE_URL = PostgreSQL connection string
SECRET_KEY = JWT signing secret
ALGORITHM = JWT algorithm (HS256)
ACCESS_TOKEN_EXPIRE_MINUTES = Token expiration

Secrets are never committed to the repository.

⸻

Project Purpose

This project was created to practice and demonstrate:
	•	REST API design
	•	Authentication and authorization
	•	Secure password handling
	•	Dependency injection
	•	Database integration
	•	Cloud deployment workflows
	•	Environment configuration
	•	Debugging real-world deployment issues
	•	Frontend ↔ backend integration