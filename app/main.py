from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


from app.api.api_v1.api import api_router
from app.config import config

# Initialize FastAPI app
app = FastAPI(
    title=config.PROJECT_NAME,
    root_path="/users",
    summary="Users Service",
    description=""" ## This service is for users managment """,
)

app.include_router(api_router)

# Configure CORS
origins = ["*", "/users"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*", "Authorization"],
    expose_headers=["*"],
)
