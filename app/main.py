import uvicorn
from fastapi import FastAPI
from app.routers import books

app = FastAPI()
app.include_router(books.router)


if __name__ == '__main__':
    # used for debugging
    uvicorn.run(app, host='0.0.0.0', port=8000)
