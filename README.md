![Tests](https://github.com/wpxq/moviesremind/actions/workflows/tests.yml/badge.svg)
# MoviesRemind [My Old Project] 

A minimalist movie watchlist to keep track of films you want to see. Built with FastAPI, SQLite, and Tailwind CSS. This project is fully "dockerized" for easy deployment.

![Preview](https://github.com/wpxq/moviesremind/blob/main/moviesremind.png)

# Tech Stack
- **Backend**: Python 3.11 + FastAPI
- **Frontend**: Jinja2 Template + Tailwind CSS (via CDN)
- **Database**: SQLite (persisted in `movies.db`)
- **Dockerized**: Docker & Docker Compose

# Setup
The simplest way to run the application is using **Docker Compose**:
```bash
docker compose up -d --build
```
The application will then be available at:
`http://localhost:8080` or if u have proxy `http://<proxy>:8080`
