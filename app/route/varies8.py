from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

varies8_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')
varies8_router.mount('/static', StaticFiles(directory='views/static'), name='static')


@varies8_router.get("/hello", response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse(
        'varies8/hello.html', {'request': req})
