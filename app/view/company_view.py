from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models import Company
from response import *
import db_connector

from service.company_service import CompanyService

router = APIRouter(prefix="/company")


class CompanyView:

    @router.post("/create_company")
    async def create_company(self, company_info: Company, session: Session = Depends(db_connector.session)):
        if not company_info.company_en and not company_info.company_ja and not company_info.company_ko:
            raise ApiException(400, INVALID_INPUT_COMPANY_NAME)
        if not company_info.tag_id:
            raise ApiException(400, INVALID_INPUT_TAG)
        if CompanyService.create_company_service(company_info, session):
            raise ApiException(200, CREATE_COMPANY)
        raise ApiException(400, CREATE_FAILED)

    @router.get("/list")
    async def list_company(self, session: Session = Depends(db_connector.session)):
        company_list = CompanyService.company_list_service(session)
        return {'data': company_list}
