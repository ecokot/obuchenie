from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str


app = FastAPI()

POSTS = {1: "Post 1", 2: "Post 2"}
def get_storage():
    print("setup")
    yield POSTS
    print("teardown")

@app.get('/posts')
def get_posts(db: dict = Depends(get_storage)):
    return list(db.values())

@app.get('/posts/{post_id}')
def get_post(post_id: int, db: dict = Depends(get_storage)):
     if post_id not in db:
         raise HTTPException(status_code=404, detail="Post not found")
     else:
         return {"id": post_id, "title": db.get(post_id, "Unknown")}

@app.post("/posts")
def create_post(post: PostCreate):
    new_id = max(POSTS.keys()) + 1 if POSTS else 1
    POSTS[new_id] = post.title
    return {"id": new_id, "title": post.title}

import time
import asyncio

@app.get("/sync-sleep")
def sync_sleep():
    time.sleep(2)
    return {"message": "sync done"}

@app.get("/async-sleep")
async def async_sleep():
    await asyncio.sleep(2)
    return {"message": "async done"}

@app.get("/async-bad")
async def async_bad():
    time.sleep(2)  # блокирует event loop!
    return {"message": "async bad done"}

@app.middleware("http")
async def log_request_time(request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    elapsed = time.perf_counter() - start
    print(f"{request.method} {request.url.path} took {elapsed:.3f}s")
    return response