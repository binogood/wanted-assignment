from fastapi import FastAPI
from dataclasses import asdict

from app.view import company_view
from app.config import conf
from app.database.conn import db


def create_app():
    app = FastAPI()
    c = conf()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)

    app.include_router(company_view.router)
    # app.include_router(tag_view.router, prefix="tag")

    @app.get("/")
    def hello_wanted():
        return "hello_wanted"

    return app


