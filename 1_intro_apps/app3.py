from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class ProfileInfo(BaseModel):
    short_description: str
    long_bio: str


class User(BaseModel):
    username: str = Field(
        alias="name",
        title="The username",
        description="this is the username of the user",
        min_length=1,
        max_length=20,
        default=None
    )
    profile_info: ProfileInfo
    liked_posts: Optional[list[int]] = Field(
        description="Array of post ids the user liked",
        min_items=2,
        max_items=10
    )


def get_user_info() -> User:
    profile_info = {
        "short_description": "My bio description",
        "long_bio": "This is our longer bio"
    }

    profile_info = ProfileInfo(**profile_info)
    user_content = {
        "liked_posts": [1] * 9,
        "profile_info": profile_info
    }

    return User(**user_content)


@app.get("/user/me", response_model=User)
def test_endpoint():
    user = get_user_info()
    return user


#   How to run?
#   uvicorn app1:app --reload
