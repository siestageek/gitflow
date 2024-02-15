from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

jjh920_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')
jjh920_router.mount('/static', StaticFiles(directory='views/static'), name='static')


@jjh920_router.get("/hello", response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse(
        'jjh920/hello.html', {'request': req})
