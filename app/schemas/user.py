from pydantic import BaseModel, Field
from typing import Optional


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


class MultipleUserResponse(BaseModel):
    users: list[FullUserProfile]
    total: int


class CreateUserResponse(BaseModel):
    user_id: int
