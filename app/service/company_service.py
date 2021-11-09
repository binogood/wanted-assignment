from app.response import *
from app.model import company_dao
from fastapi.responses import JSONResponse


async def create_company_service(company_info, x_wanted_language, session):
    lang_id = company_dao.find_language_dao(x_wanted_language, session)

    if not lang_id:
        lang_id = company_dao.create_language_dao(x_wanted_language, session)
        company_dao.create_tag_dao(lang_id, session)
    company_id = company_dao.create_company_dao(session)

    for tag in company_info.tags:
        tag_name = tag.tag_name.ko
        tag_id = company_dao.find_tag_dao(tag_name, session)
        company_dao.create_company_tag_dao(company_id, tag_id, session)

    for i in company_info.company_name:
        lang_id = company_dao.find_language_dao(i[0], session)
        company_dao.create_company_language_dao(company_id, lang_id, i[1], session)

    temp_dic = {
        'company_id': company_id
    }

    return temp_dic


def company_search_service(company_name, x_wanted_language, session):
    company_id = company_dao.find_company_id_dao(company_name, session)
    if not company_id:
        return JSONResponse(status_code=404, content='실패')
    lang_id = company_dao.find_language_dao(x_wanted_language, session)
    if not lang_id:
        return JSONResponse(status_code=404, content='실패')
    tag_list = company_dao.find_tag_all_dao(company_id, session)
    company = company_dao.find_company_dao(company_id, lang_id, session)
    result = {'company_name': company}
    tags = []
    for idx in range(len(tag_list)):
        tag_name = company_dao.find_tag_name_dao(tag_list[idx][0], lang_id, session)
        tags.append(tag_name)

    result['tags'] = tags
    return result


def find_company_service(temp_dict, x_wanted_language, session):
    lang_id = company_dao.find_language_dao(x_wanted_language, session)
    tag_list = company_dao.find_tag_all_dao(temp_dict['company_id'], session)

    tags = []
    for idx in range(len(tag_list)):
        tag_name = company_dao.find_tag_name_dao(tag_list[idx][0], lang_id, session)
        tags.append(tag_name)

    company = company_dao.find_company_name_dao(temp_dict['company_id'], lang_id, session)
    result = {'company_name': company}
    result['tags'] = tags
    return result
