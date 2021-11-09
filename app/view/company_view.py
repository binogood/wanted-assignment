from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from typing import Optional
from fastapi.encoders import jsonable_encoder

from app.models import Company
from app.response import *
from app.database.conn import db

from app.service import company_service

router = APIRouter()


@router.post("/companies")
async def create_company(company_info: Company, x_wanted_language: Optional[str] = Header('ko'),
                         session: Session = Depends(db.session)):
    if not company_info.company_name:
        raise ApiException(404, INVALID_INPUT_COMPANY_NAME)
    if not company_info.tags:
        raise ApiException(404, INVALID_INPUT_TAG)
    if await company_service.create_company_service(company_info, x_wanted_language, session):
        return True
    raise ApiException(400, CREATE_FAILED)


@router.get("/companies/{company_name}")
async def list_company(x_wanted_language: Optional[str] = Header('ko'), company_name: Optional[str] = None,
                       session: Session = Depends(db.session)):
    company = company_service.company_search_service(company_name, x_wanted_language, session)
    return company

  
@router.get("/search")
async def name_autocomplete_company(query : Optional[str], request:Request, session: Session = Depends(db.session)):
    lang = request.headers.get("x-wanted-language")
    data = await company_service.company_automatch_service(query, lang, session)
    if data:
        return data
    return ApiException(404, SEARCH_FAILED)
