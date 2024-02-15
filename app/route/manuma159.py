from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

manuma159_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')
manuma159_router.mount('/static', StaticFiles(directory='views/static'), name='static')


@manuma159_router.get("/hello", response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse(
        'manuma159/hello.html', {'request': req})
