from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from app.route.bamyam import bamyam_router
from app.route.index import index_router
#<<<<<<< muhotalgo
from app.route.muhotalgo import muhotalgo_router
#=======
from app.route.varies8 import varies8_router
from app.route.yunsung22 import yunsung22_router
from app.route.redraoh import redraoh_router
from app.route.jjh920 import jjh920_router
from app.route.zzyzzy import zzyzzy_router
#>>>>>>> main

app = FastAPI()

# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
app.mount('/static', StaticFiles(directory='views/static'), name='static')

# 외부 route 파일 불러오기
app.include_router(index_router)
# <<<<<<< bamyam
app.include_router(bamyam_router, prefix='/bamyam')
#=======
app.include_router(muhotalgo_router, prefix='/muhotalgo')
app.include_router(varies8_router, prefix='/varies8')
app.include_router(yunsung22_router, prefix='/yunsung_router')
app.include_router(redraoh_router, prefix='/redraoh')
app.include_router(jjh920_router, prefix='/jjh920')
app.include_router(zzyzzy_router, prefix='/zzyzzy')
#>>>>>>> main

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', reload=True)
