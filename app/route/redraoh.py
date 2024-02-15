from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

redraoh_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')
redraoh_router.mount('/static', StaticFiles(directory='views/static'), name='static')


@redraoh_router.get("/hello", response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse(
        'redraoh/hello.html', {'request': req})
