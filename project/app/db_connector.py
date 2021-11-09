# from fastapi import FastAPI
# from pydantic import BaseModel
# import pymysql
#
# # from app.config import DATABASE
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
#
# DB_URL = f"mysql+pymysql://{DATABASE['user']}:{DATABASE['password']}@localhost/\
#             {DATABASE['database']}?charset={DATABASE['charset']}"
# engine = create_engine(DB_URL)
# session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
# base = declarative_base()
#
#
# def get_db():
#     db = session()
#     try:
#         yield db
#     finally:
#         db.close()
#
