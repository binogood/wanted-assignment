from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models import Tag
from app import db_connector
from app.response import *

from app.service.tag_service import TagService

router = APIRouter(prefix="/tag")

class TagView:
    def __init__(self):
        pass

    def create_tag_view(self, session: Session = Depends(db_connector.session)):
        tag_id = TagService.create_tag_service(session)
        if tag_id:
            raise ApiException(200, CREATE_TAG)
        raise ApiException(400, CREATE_FAILED)
