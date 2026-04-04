import pytest
from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_read_main():
    resp = client.get("/")
    assert resp.status_code == 200
    assert "Watchlist" in resp.text

def test_add_movie():
    resp = client.post("/add", json={"title": "Inception"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["title"] == "Inception"
    assert "id" in data
    
def test_delete_movie():
    add_res = client.post("/add", json={"title": "DeleteMe"})
    movie_id = add_res.json()["id"]
    resp = client.get(f"/delete/{movie_id}", follow_redirects=False)
    assert resp.status_code == 303
    assert resp.headers["location"] == "/"
    
if __name__ == "__main__":
    test_read_main()
    test_add_movie()
    test_delete_movie()