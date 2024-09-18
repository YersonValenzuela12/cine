from fastapi import FastAPI
from pydantic import BaseModel

# instanciaciamos  fastapi
app = FastAPI()

class Post(BaseModel):
    autor:str
    title:str
    content:str

@app.get("/")
async def root():
    return {"name":"Grupo 2"}

@app.post('/posts')
async def viewPost(post: Post):
    return {"alert": f"el post de {post.title} ha sido agregado"}
