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
from sqlalchemy.orm import Session, relationship
from app.db_connector import base


class Company(base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True, index=True)
    create_at = Column(DateTime, nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp())
    update_at = Column(DateTime, nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp())


class Tag(base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, index=True)


class CompanyTag(base):
    __tablename__ = 'company_tag'
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey(Company.id))
    tag_id = Column(Integer, ForeignKey(Tag.id))

    company = relationship("Company", back_populates="Company")
    tag = relationship("Tag", back_populates="Tag")


class Language(base):
    __tablename__ = 'language'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=50), nullable=False)


class CompanyLanguageName(base):
    __tablename__ = 'company_language_name'
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey(Company.id))
    language_id = Column(Integer, ForeignKey(Language.id))
    company_name = Column(String(length=50), nullable=False)

    company = relationship("Company", back_populates="Company")
    language = relationship("Language", back_populates="Language")


class TagLanguageName(base):
    __tablename__ = 'tag_language_name'
    id = Column(Integer, primary_key=True, index=True)
    tag_id = Column(Integer, ForeignKey(Tag.id))
    language_id = Column(Integer, ForeignKey(Language.id))
    tag_name = Column(String(length=50), nullable=False)

    tag = relationship("Tag", back_populates="Tag")
    language = relationship("Language", back_populates="Language")