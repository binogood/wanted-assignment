from fastapi import FastAPI
from view import company_view


def create_app():
    app = FastAPI()

    app.include_router(company_view.router, prefix="/api")
    # app.include_router(tag_view.router, prefix="tag")
    @app.get("/")
    def hello_wanted():
        return "hello_wanted"

    return app


