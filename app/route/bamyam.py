from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

bamyam_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')
bamyam_router.mount('/static', StaticFiles(directory='views/static'), name='static')


@bamyam_router.get("/hello", response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse(
        'bamyam/hello.html', {'request': req})
