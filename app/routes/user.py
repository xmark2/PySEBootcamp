from fastapi import APIRouter, Depends
from app.schemas.user import (
    CreateUserResponse,
    FullUserProfile,
    MultipleUserResponse)
from app.services.user import UserService
import logging
from app.dependencies import rate_limit
from app.clients.db import DatabaseClient

logger = logging.getLogger(__name__)


def create_user_router(database_client: DatabaseClient) -> APIRouter:
    router = APIRouter(
        prefix="/user",
        tags=["user"],
        dependencies=[Depends(rate_limit)]
    )
    user_services = UserService(database_client)

    @router.get("/all", response_model=MultipleUserResponse)
    async def get_all_users_paginated(start: int = 0, limit: int = 2):
        users, total = await user_services.get_all_users_with_pagination(start, limit)
        formatted_users = MultipleUserResponse(users=users, total=total)
        return formatted_users

    @router.get("/{user_id}", response_model=FullUserProfile)
    async def get_user_by_id(user_id: int):
        """
        Endpoint for retrieving a FullUserProfile by the user's unique integer id
        :param user_id: int - unique monotonically increasing integer id
        :return: FullUserProfile
        """
        # rate_limit(response)
        full_user_profile = await user_services.get_user_info(user_id)
        return full_user_profile

    @router.put("/{user_id}")
    async def update_user(user_id: int, full_profile_info: FullUserProfile):
        await user_services.create_update_user(full_profile_info, user_id)
        return None

    @router.delete("/{user_id}")
    async def remove_user(user_id: int):
        await user_services.delete_user(user_id)

    @router.post('/', response_model=CreateUserResponse, status_code=201)
    async def add_user(full_profile_info: FullUserProfile):
        user_id = await user_services.create_update_user(full_profile_info)
        print("doc string of create_update_user:\n", user_services.create_update_user.__doc__)
        created_user = CreateUserResponse(user_id=user_id)
        return created_user

    return router
