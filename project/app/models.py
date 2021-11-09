from pydantic import BaseModel
from typing import Optional, List


class Tag(BaseModel):
    ko: str = '태그_1'
    en: str = 'tag_1'
    ja: str = 'タグ_1'


class TagName(BaseModel):
    tag_name: Optional[Tag] = None


class CompanyName(BaseModel):
    ko: str = '원티드'
    en: str = 'wanted'
    ja: str = ''


class Company(BaseModel):
    company_name: Optional[CompanyName] = None
    tags: Optional[List[TagName]] = None


class CompanyLanguage(BaseModel):
    Language: str = None


class Language(BaseModel):
    name: str = None