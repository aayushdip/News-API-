from fastapi import APIRouter, Query, status, HTTPException
from typing import List, Union
import edgedb
from queries import (
    create_user_async_edgeql as create_user_qry,
    get_subscriber_list_async_edgeql as get_user_subscriber_qry,
    get_user_by_username_async_edgeql as get_user_with_username_qry,
    get_users_async_edgeql as get_user_all_list_qry,
)
from schemas.user_schema import UserCreate, UserRead
from hashing_password import hash_password

router = APIRouter()
client = edgedb.create_async_client()


@router.get("/users", response_model=Union[List[UserRead], UserRead])
async def get_users(
    username: str = Query(None, max_length=50)
) -> Union[
    List[get_user_all_list_qry.GetUsersResult],
    get_user_with_username_qry.GetUserByUsernameResult,
]:
    """
    Get users by their usernames or all users if username is not provided.
    """
    if not username:
        users = await get_user_all_list_qry.get_users(client)
        return users
    else:
        user = await get_user_with_username_qry.get_user_by_username(
            client, arg0=username
        )
        return user


@router.get("/subscribers", response_model=List[UserRead])
async def get_subscribers() -> get_user_subscriber_qry.GetSubscriberListResult:
    """
    Get a list of subscribers.
    """
    subscribers = await get_user_subscriber_qry.get_subscriber_list(client)
    return subscribers


@router.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate) -> create_user_qry.CreateUserResult:
    """
    Create a new user.
    """
    try:
        created_user = await create_user_qry.create_user(
            client,
            name=user.name,
            email=user.email,
            username=user.username,
            admin=user.admin,
            subscriber=user.subscriber,
            hashed_password=hash_password(user.hashed_password),
        )
    except edgedb.errors.ConstraintViolationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": f"Username '{user.name}' already exists."},
        )
    return created_user
