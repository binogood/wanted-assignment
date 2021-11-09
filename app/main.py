from fastapi import FastAPI
from dataclasses import asdict

from view import company_view
from config import conf
from database.conn import db

description = """
# [Assignment 3] 원티드랩 과제


### 팀원 : 강대훈, 김훈태, 안다민, 이무현, 송빈호, 정성헌

"""

def create_app():
    app = FastAPI(title="Wantedlab Restfull API",
                  description=description)
    c = conf()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)

    app.include_router(company_view.router)
    #app.include_router(tag_view.router, prefix="tag")

    return app


