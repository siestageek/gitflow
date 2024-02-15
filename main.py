from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from app.route.manuma159 import manuma159_router

app = FastAPI()

# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
app.mount('/static', StaticFiles(directory='views/static'), name='static')

# 외부 route 파일 불러오기

app.include_router(manuma159_router, prefix='manuma159')


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)
