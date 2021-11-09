from app.database.schema import (
    Company,
    Language,
    CompanyLanguageName,
    TagLanguageName,
    Tag,
    CompanyTag
)


def find_language_dao(x_wanted_language, session):
    lang_id = session.query(Language.id).filter(Language.name == x_wanted_language).first()
    if lang_id:
        return lang_id[0]
    return False


def create_language_dao(x_wanted_language, session):
    create_lang = Language(name = x_wanted_language)
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


def find_tag_all_dao(company_id, session):
    tag_list = session.query(CompanyTag.tag_id).filter(CompanyTag.company_id == company_id).all()
    return tag_list


def find_tag_name_dao(tag_id, session):
    tag_name = session.query(TagLanguageName.tag_name).filter(TagLanguageName.tag_id == tag_id).first()
    print(tag_name)
    return tag_name[0]


def create_company_dao(session):
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


def find_company_id_dao(company_name, session):
    company = session.query(CompanyLanguageName.company_id).\
        filter(CompanyLanguageName.company_name == company_name).first()
    if company:
        return company[0]
    return False

def find_company_dao(company_id, lang_id, session):
    company = session.query(CompanyLanguageName.company_name).filter(CompanyLanguageName.company_id == company_id,
                                                                     CompanyLanguageName.language_id == lang_id)
    return company[0][0]


def autocomplete_company_language_dao(query, lang, session):
    company_names = []
    lang_id = find_language_dao(lang, session)

    company_name = session.query(CompanyLanguageName.company_name).filter(
                                                 CompanyLanguageName.company_name.like('%' + query + '%')&
                                                CompanyLanguageName.language_id == lang_id).all()
    for i in company_name:
        company_names.append(i[0])
    return company_names


