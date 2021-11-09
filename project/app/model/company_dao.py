from app.database.schema import Company, Language, CompanyLanguageName, TagLanguageName, Tag, CompanyTag


    # def find_company_name_dao(self, company_info, session):
    #     get_company = session.query.filter(ComapanyLanguage.company_name in company_info.company_name)
    #     return get_company

def find_language_dao(lang, session):
    lang_id = session.query(Language.id).filter(Language.name == lang).first()
    if lang_id:
        return lang_id[0]
    return False

def create_language_dao(lang, session):
    create_lang = Language(name = lang)
    session.add(create_lang)
    session.commit()
    session.refresh(create_lang)
    return create_lang.id


def create_tag_dao(lang_id, session):
    for tag_num in range(1, 31):
        create_tag = TagLanguageName(tag_id=tag_num, language_id=lang_id, tag_name=f'tag_{tag_num}')
        session.add(create_tag)
        session.commit()
        session.refresh(create_tag)

    return True


def create_company_tag_dao(company_id, tag_id, session):
    company_tag = CompanyTag(company_id=company_id, tag_id=tag_id)
    session.add(company_tag)
    session.commit()
    session.refresh(company_tag)
    return company_tag


def find_tag_dao(tag_name, session):
    tag_id = session.query(TagLanguageName.id).filter(TagLanguageName.tag_name == tag_name).first()
    return tag_id[0]


def create_company_dao(company_info, session):
    create_company = Company()
    session.add(create_company)
    session.commit()
    session.refresh(create_company)
    return create_company.id


def create_company_language_dao(company_id, lang_id, company_name, session):
    company_language_name = CompanyLanguageName(company_id = company_id, company_name = company_name,
                                                language_id = lang_id)
    session.add(company_language_name)
    session.commit()
    session.refresh(company_language_name)
    return True
# def company_list_dao(lang, session):
#     company_list = session.query(Company)
#     return company_list


    # def company_search_list_dao(self, q, lang, session):
    #     if lang == "ko"
    #         company_search_list = session.query(Company).filter(Company.)
    #     elif lang == "en"
    #
    #     elif lang == ""