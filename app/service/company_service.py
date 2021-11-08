from app.response import *
from app.model.company_dao import CompanyDao


class CompanyService:
    def __init__(self):
        pass

    def find_company_name_service(self, company_info, session):
        if CompanyDao.find_company_name_dao(company_info, session):
            raise ApiException(400, ALREADY_EXISTS_COMPANY_NAME)

    def create_company_service(self, company_info, session):
        company_id = CompanyDao.create_company_dao(company_info, session)
        return company_id

    def company_list_service(self, session):
        compant_list = CompanyDao.company_list_dao(session)
        return compant_list
