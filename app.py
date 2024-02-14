from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata

app = FastAPI(
    title="Rest Api test python - mongodb",
    description="this is a simple Rest Api using fastApi andMongoDb Anaconde virtual env",
    version="0.0.1",
    openapi_tags=tags_metadata
) 


app.include_router(user)


