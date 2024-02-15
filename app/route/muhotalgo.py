from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

muhotalgo_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')
muhotalgo_router.mount('/static', StaticFiles(directory='views/static'), name='static')


@muhotalgo_router.get("/hello", response_class=HTMLResponse)
async def muhotalgo(req: Request):
    return templates.TemplateResponse(
        'muhotalgo/hello.html', {'request': req})
