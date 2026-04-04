from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
import sqlite3

app = FastAPI()
templates = Jinja2Templates(directory="templates")
db_f = Path("movies.db")

def get_db():
    conn = sqlite3.connect(db_f)
    conn.row_factory = sqlite3.Row
    return conn

@app.on_event("startup")
def startup():
    db = get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    """)
    db.commit()
    db.close()

@app.get("/")
def movies(request: Request):
    db = get_db()
    movies = db.execute("SELECT * FROM movies").fetchall()
    db.close()
    #return templates.TemplateResponse("movies.html", {"request": request, "movies": movies})
    return templates.TemplateResponse(
        request=request, 
        name="movies.html", 
        context={"movies": movies}
    )

@app.post("/add")
async def add_movie(request: Request):
    data = await request.json()
    title = data.get("title")
    if not title:
        return JSONResponse({"error": "No title"}, status_code=400)
    db = get_db()
    cursor = db.execute("INSERT INTO movies (title) VALUES (?)", (title,))
    db.commit()
    new_id = cursor.lastrowid
    db.close()
    return {"id": new_id, "title": title} 

@app.get("/delete/{movie_id}")
def delete_movie(movie_id: int):
    db = get_db()
    db.execute("DELETE FROM movies WHERE id=?", (movie_id,))
    db.commit()
    db.close()
    return RedirectResponse("/", status_code=303)