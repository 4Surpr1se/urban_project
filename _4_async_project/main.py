from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api import user
from core.config import get_project_config
from core.lifespan import lifespan

project_config = get_project_config()

app = FastAPI(
    title=project_config.project_name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
    lifespan=lifespan
)

app.include_router(user.router, prefix='', tags=['user'])