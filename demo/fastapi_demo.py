from fastapi import FastAPI, Depends
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
    return {"id": post_id, "title": db.get(post_id, "Unknown")}

@app.post("/posts")
def create_post(post: PostCreate):
    new_id = max(POSTS.keys()) + 1 if POSTS else 1
    POSTS[new_id] = post.title
    return {"id": new_id, "title": post.title}

