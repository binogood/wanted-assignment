from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from typing import Optional
from fastapi.encoders import jsonable_encoder

from app.models import Company
from app.response import *
from app.database.conn import db

from app.service import company_service

router = APIRouter()
# router = APIRouter(prefix="/company")


# @router.post("/test")
# async def create_company(company_info: Company,lang: Optional[str] = Header('ko'),
#                          session: Session = Depends(db.session)):
#     print(jsonable_encoder(company_info.company_name), lang, session)
#     for i in company_info.company_name:
#         print(i[0])
# # {'company_name': {'ko': '원티드', 'en': 'wanted', 'ja': 'string'},
# # 'tags': [{'tag_name': {'ko': '태그_1', 'en': 'tag_1', 'ja': 'string'}}]}


@router.post("/companies")
async def create_company(company_info: Company, lang: Optional[str] = Header('ko'),
                         session: Session = Depends(db.session)):
    if not company_info.company_name:
        raise ApiException(404, INVALID_INPUT_COMPANY_NAME)
    if not company_info.tags:
        raise ApiException(404, INVALID_INPUT_TAG)
    if await company_service.create_company_service(company_info, lang, session):
        return 1
        # raise ApiException(200, CREATE_COMPANY)
    raise ApiException(400, CREATE_FAILED)


# @router.get("/companies/{company_name}")
# async def list_company(company_name, lang: Optional[str] = Header(None),
#                        session: Session = Depends(db_connector.session)):
#     if not company_name:
#         raise ApiException(404, INVALID_INPUT_COMPANY_NAME)
#     company_list = company_service.company_list_service(company_name, lang, session)
#     return {'data': company_list}
#
#
# @router.get("/search")
# async def get_company(query: Optional[str] = None, lang: Optional[str] = Header(None),
#                       session: Session = Depends(db_connector.session)):
#     if not query:
#         raise ApiException (404, INVALID_INPUT_COMPANY_NAME)
#     company_search_list = company_service.company_search_list_service(query, lang, session)
#     return company_search_list






# class CompanyView:
#     def __init__(self):
#         pass
#
#     @router.post("/test")
#     async def create_company(self, company_info: Company):
#         print(11111, company_info)
#
#     @router.post("/companies")
#     async def create_company(self, company_info: Company, lang: Optional[str] = Header('ko'),
#                              session: Session = Depends(db_connector.session)):
#         print(company_info)
#         if not company_info.company_name:
#             raise ApiException(404, INVALID_INPUT_COMPANY_NAME)
#         if not company_info.tags:
#             raise ApiException(404, INVALID_INPUT_TAG)
#         if CompanyService.create_company_service(company_info, lang, session):
#             raise ApiException(200, CREATE_COMPANY)
#         raise ApiException(400, CREATE_FAILED)
#
#     @router.get("/companies/{company_name}")
#     async def list_company(self, company_name, lang: Optional[str] = Header(None),
#                            session: Session = Depends(db_connector.session)):
#         if not company_name:
#             raise ApiException(404, INVALID_INPUT_COMPANY_NAME)
#         company_list = CompanyService.company_list_service(company_name, lang, session)
#         return {'data': company_list}
#
#     @router.get("/search")
#     async def get_company(self, query: Optional[str] = None, lang: Optional[str] = Header(None),
#                           session: Session = Depends(db_connector.session)):
#         if not query:
#             raise ApiException (404, INVALID_INPUT_COMPANY_NAME)
#         company_search_list = CompanyService.company_search_list_service(query, lang, session)
#         return company_search_list
#
