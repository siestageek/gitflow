from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

siestageek_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')
siestageek_router.mount('/static', StaticFiles(directory='views/static'), name='static')


@siestageek_router.get("/hello", response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse(
        'siestageek/hello.html', {'request': req})
