# NotesVault API

🚀 Live demo: https://notesvault-api.onrender.com

NotesVault is a backend REST API that allows users to register, authenticate, and manage private notes.  
Each user can only access their own data.

This project was built as a **portfolio project** to demonstrate real-world backend development and deployment practices.

---

## Features

- User registration and login
- JWT-based authentication (OAuth2 password flow)
- Protected endpoints
- User-scoped data access
- PostgreSQL database
- Dockerized application
- CI pipeline with GitHub Actions
- Cloud deployment with health checks

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT (OAuth2)
- Docker
- GitHub Actions
- Render (deployment)

---

## Live API

The API is deployed and publicly accessible.

- Health check endpoint  
  `GET /healthz`

- Interactive API documentation (Swagger UI)  
  `GET /docs`

Using Swagger, you can:
1. Register a new user
2. Log in with email and password
3. Authorize using the Bearer token
4. Create new notes
5. List your existing notes

---

## Running Locally with Docker

### Prerequisites
- Docker installed and running

### Build the Docker image

### bash
docker build -t notesvault-api .
---

 Project Purpose

This project was created to practice and demonstrate:
	•	REST API design
	•	Authentication and authorization
	•	Secure password handling
	•	Dependency injection and request lifecycle
	•	Database integration with PostgreSQL
	•	Containerization using Docker
	•	Continuous integration pipelines
	•	Cloud deployment and environment configuration
	•	Debugging real-world deployment issues

⸻

 Architecture Overview
	•	The application is stateless.
	•	Authentication is handled using JWT tokens.
	•	All persistent data is stored in PostgreSQL.
	•	Secrets are injected via environment variables.
	•	Health check endpoints are included for cloud platform compatibility.

⸻

Notes
	•	Database credentials and secrets are not committed to the repository.
	•	The application can be redeployed without data loss when connected to an external database.
	•	The project intentionally focuses on backend and deployment concerns rather than frontend UI.

⸻

Status

This project is considered complete and maintained as a portfolio reference.
