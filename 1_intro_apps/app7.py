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
        default=None
    )
    liked_posts: Optional[list[int]] = Field(
        description="Array of post ids the user liked",
    )


class FullUserProfile(User):
    short_description: str
    long_bio: str


def get_user_info(user_id: str = "default") -> FullUserProfile:
    profile_infos = {
        "default": {
                    "short_description": "My bio description",
                    "long_bio": "This is our longer bio"
                    },
        "user_1": {
                    "short_description": "User 1's bio description",
                    "long_bio": "User 1's longer bio"
                }
    }

    profile_info = profile_infos[user_id]
    users_content = {
        "default": {"liked_posts": [1] * 9,
                    "profile_info": profile_info
                    },
        "user_1": {"liked_posts": [],
                    "profile_info": profile_info
                    }
    }

    user_content = users_content[user_id]
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


@app.get("/user/{user_id}", response_model=FullUserProfile)
def get_user_by_id(user_id: str):
    full_user_profile = get_user_info(user_id)
    return full_user_profile


#   How to run?
#   uvicorn app1:app --reload
