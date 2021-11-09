from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from typing import Optional
from fastapi.encoders import jsonable_encoder

from app.models import Company
from app.response import *
from app.database.conn import db

from app.service import company_service

router = APIRouter()

class CompanyView:

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

    @router.get("/list")
    async def list_company(self, session: Session = Depends(db_connector.session)):
        company_list = CompanyService.company_list_service(session)
        return {'data': company_list}
