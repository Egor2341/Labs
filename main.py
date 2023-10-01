from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel

app = FastAPI()


class Wiki(BaseModel):
    search: str
    sentences: int


class Request(BaseModel):
    search: str


@app.get("/")
def hello():
    return 'Hello!'


@app.get("/{search}")
def request(search: str):
    return wikipedia.summary(search)


@app.get("/extra/{search}")
def quantity(search: str, sentences: int):
    try:
        return wikipedia.summary(search, sentences=sentences)
    except:
        return 'Nothing found'


@app.post("/", response_model=Wiki)
def create_req(request: Request, sentences: int):
    return Wiki(search=request.search, sentences=sentences)
