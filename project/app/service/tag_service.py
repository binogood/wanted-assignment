from app.response import *
from app.model.tag_dao import TagDao

class TagService:
    def __init__(self):
        pass

    def create_tag_service(self, session):
        last_tag_number_id = TagDao.find_tag_dao(session):
        if not last_tag_number_id:
            tag_info = {
                tag_ko =
            }
            new_tag = TagDao.create_tag_dao(session)

