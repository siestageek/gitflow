from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

index_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')
index_router.mount('/static', StaticFiles(directory='views/static'), name='static')


@index_router.get("/", response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse(
        'index.html', {'request': req})
