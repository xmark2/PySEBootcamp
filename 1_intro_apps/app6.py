from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class User(BaseModel):
    username: str = Field(
        alias="name",
        title="The username",
        description="this is the username of the user",
        min_length=1,
        max_length=20,
        default=None
    )
    liked_posts: Optional[list[int]] = Field(
        description="Array of post ids the user liked",
        min_items=2,
        max_items=10
    )


class FullUserProfile(User):
    short_description: str
    long_bio: str


def get_user_info() -> FullUserProfile:
    profile_info = {
        "short_description": "My bio description",
        "long_bio": "This is our longer bio"
    }

    user_content = {
        "liked_posts": [1] * 9,
        "profile_info": profile_info
    }
    user = User(**user_content)

    full_user_profile = {
        **profile_info,
        **user.dict()
    }

    return FullUserProfile(**full_user_profile)


@app.get("/user/me", response_model=FullUserProfile)
def test_endpoint():
    full_user_profile = get_user_info()
    return full_user_profile


#   How to run?
#   uvicorn app1:app --reload
