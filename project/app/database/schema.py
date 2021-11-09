
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
from sqlalchemy.orm import relationship
from app.database.conn import base


class Company(base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True, index=True)
    create_at  = Column(DateTime, nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp())
    update_at  = Column(DateTime, nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp())


class Tag(base):
    __tablename__ = 'tag'
    id            = Column(Integer, primary_key=True, index=True)


class CompanyTag(base):
    __tablename__ = 'company_tag'
    id            = Column(Integer, primary_key=True, index=True)
    company_id    = Column(Integer, ForeignKey("company.id"), nullable=False)
    tag_id        = Column(Integer, ForeignKey("tag.id"), nullable=False)

    # company = relationship("Company", backref="company")
    # tag     = relationship("Tag", backref="tag")


class Language(base):
    __tablename__ = 'language'
    id   = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=50), nullable=False)


class CompanyLanguageName(base):
    __tablename__ = 'company_language_name'
    id            = Column(Integer, primary_key=True, index=True)
    company_id    = Column(Integer, ForeignKey("company.id"), nullable=False)
    language_id   = Column(Integer, ForeignKey("language.id"), nullable=False)
    company_name  = Column(String(length=50), nullable=False)
    #
    # company = relationship("Company", back_populates="company_language_name")
    # language = relationship("Language", backref="language")


class TagLanguageName(base):
    __tablename__ = 'tag_language_name'
    id          = Column(Integer, primary_key=True, index=True)
    tag_id      = Column(Integer, ForeignKey("tag.id"), nullable=False)
    language_id = Column(Integer, ForeignKey("language.id"), nullable=False)
    tag_name    = Column(String(length=50), nullable=False)
    #
    # tag = relationship("Tag", backref="tag")
    # language = relationship("Language", backref="language")



