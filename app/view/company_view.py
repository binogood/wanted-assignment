from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from typing import Optional
from fastapi.responses import JSONResponse

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
    temp_dict = await company_service.create_company_service(company_info, x_wanted_language, session)
    data = company_service.find_company_service(temp_dict, x_wanted_language, session)
    if data:
        return data
    return JSONResponse(status_code=404, content='실패')


@router.get("/companies/{company_name}")
async def list_company(x_wanted_language: Optional[str] = Header('ko'), company_name: Optional[str] = None,
                       session: Session = Depends(db.session)):
    data = company_service.company_search_service(company_name, x_wanted_language, session)
    if data:
        return data
    return JSONResponse(status_code=404, content='실패')