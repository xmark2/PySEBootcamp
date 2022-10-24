from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class User(BaseModel):
    username: str
    short_description: str
    liked_posts: Optional[list] = None


def get_user_info() -> (str, str):
    username = "testuser"
    short_description = "My bio description"
    liked_posts = []
    return username, short_description, liked_posts


@app.get("/user/me", response_class=JSONResponse)
def test_endpoint():

    username, short_description, liked_posts = get_user_info()

    user = User(username=username, short_description=short_description, liked_posts=liked_posts)

    return user


#   How to run?
#   uvicorn app1:app --reload
