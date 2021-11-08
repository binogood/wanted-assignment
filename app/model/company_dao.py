from app.database.schema import Company


class CompanyDao:
    def __init__(self):
        pass

    def find_company_name_dao(self, company_info, session):
        get_company = session.query.filter(Company.company_ko == company_info['company_ko'] |
                                           Company.company_ja == company_info['company_ja'] |
                                           Company.company_en == company_info['company_en'])
        return get_company

    def create_company_dao(self, company_info, session):
        create_company = Company(company_ko=company_info.company_ko, company_ja=company_info.company_ja,
                                 company_en=company_info.company_en, tag_id=company_info.tag_id)
        session.add(create_company)
        session.commit()
        session.refresh(create_company)
        return create_company

    def company_list_dao(self, session):
        company_list = session.query(Company)
        return company_list