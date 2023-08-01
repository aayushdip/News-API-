from fastapi import Depends, APIRouter, status, HTTPException, Query
from http import HTTPStatus
from queries import (
    create_user_async_edgeql as create_user_qry,
    get_subscriber_list_async_edgeql as get_user_subscriber_qry,
    get_user_by_username_async_edgeql as get_user_with_username_qry,
    get_users_async_edgeql as get_user_all_list_qry,
)
from schemas.user_schema import UserCreate, UserInDB, UserRead
from hashing_password import hash_password
import edgedb

router = APIRouter()
client = edgedb.create_async_client()


@router.post("/users", status_code=status.HTTP_201_CREATED)
async def post_user(user: UserCreate) -> create_user_qry.CreateUserResult:
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


print("hello")
