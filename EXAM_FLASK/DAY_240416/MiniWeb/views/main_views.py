### 기능 : main 범주의 url 의 라우팅
###  URL : /main, /main/info, .main/about, ...

from flask import Blueprint

bp = Blueprint(__name__, url_prefix='/main/')

@bp.route('about')
def main_about():
    return 'ABOUT MAIN'