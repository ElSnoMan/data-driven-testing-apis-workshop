from fastapi import APIRouter

from app.mocks import FASTAPI_MOCKED_BOOKS

router = APIRouter()


@router.get('/books/', tags=['books'])
async def get_all_books():
    return FASTAPI_MOCKED_BOOKS


# @router.get("/users/{username}", tags=["users"])
# async def read_user(username: str):
#     return {"username": username}
