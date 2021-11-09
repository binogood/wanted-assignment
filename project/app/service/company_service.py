from app.response import *
from app.model import company_dao


async def create_company_service(company_info, lang, session):

    lang_id = company_dao.find_language_dao(lang, session)

    if not lang_id:
        lang_id = company_dao.create_language_dao(lang, session)
        company_dao.create_tag_dao(lang_id, session)

    company_id = company_dao.create_company_dao(company_info, session)

    for tag in company_info.tags:
        tag_name = tag.tag_name.ko
        tag_id = company_dao.find_tag_dao(tag_name, session)
        company_dao.create_company_tag_dao(company_id, tag_id, session)

    for i in company_info.company_name:
        lang_id = company_dao.find_language_dao(i[0], session)
        company_dao.create_company_language_dao(company_id, lang_id, i[1], session)

    return True


# async def company_list_service(lang ,session):
#     compant_list = await company_dao.company_list_dao(lang ,session)
#     return compant_list
#
#
# async def company_search_list_service(q, lang, session):
#     company_search_list = await company_dao.company_search_list_dao(q, lang, session)
#     return company_search_list