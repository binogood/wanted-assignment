
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
    Enum,
    Boolean,
    ForeignKey
)
from sqlalchemy.orm import Session,relationship
from app.db_connector import base


class Tag(base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, index=True)
    tag_ko = Column(String(length=10), nullable=False)
    tag_en = Column(String(length=10), nullable=False)
    tag_ja = Column(String(length=10), nullable=False)


class Company(base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True, index=True)
    ko = Column(String(length=50), nullable=False)
    en = Column(String(length=100), nullable=False)
    ja = Column(String(length=50), nullable=False)
    tag_id     = Column(Integer, ForeignKey(Tag.id))
    create_at  = Column(DateTime, nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp())
    update_at  = Column(DateTime, nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp())

    tag = relationship("Tag", back_populates="owner")


