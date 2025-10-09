# Todo List Application

A full-stack Todo List web application built with Django, PostgreSQL, and Docker. This project demonstrates modern web development practices with containerization for consistent deployment.

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

## 🚀 Features

- ✅ Create, read, update, and delete todo items
- 📝 Mark tasks as complete/incomplete (in updates)
- 🎨 Clean and responsive user interface
- 🗃️ PostgreSQL database for reliable data storage
- 🐳 Docker containerization for easy deployment
- 🔄 RESTful architecture

## 🛠️ Tech Stack

### Backend
- **Framework:** Django 4.2+
- **Language:** Python 3.9+
- **Database:** PostgreSQL
- **ORM:** Django ORM

### Frontend
- **Templating:** Django Templates
- **Styling:** Custom CSS
- **Markup:** HTML5

### DevOps
- **Containerization:** Docker & Docker Compose
- **Environment Management:** Python Decouple

## 📋 Prerequisites

Before running this project, make sure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## 🏃‍♂️ Quick Start

### Using Docker (Recommended)
1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd todo-project
   ```
2. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   **Edit .env with your configuration:**
   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   DB_NAME=todo_db
   DB_USER=postgres
   DB_PASSWORD=password
   DB_HOST=db
   DB_PORT=5432
   ```
3. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```
4. **Run database migrations**
   ```bash
   docker-compose exec web python manage.py migrate
   ```
5. Access the application <br>
   Open your browser and navigate to: http://localhost:8000
   
## 👨‍💻 Author

### Mohammadrafie Fatahinia

### GitHub: @Seyed-Rafie

### LinkedIn: https://www.linkedin.com/in/mohammadrafie-fatahinia/