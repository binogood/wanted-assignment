from pydantic.main import BaseModel


class Company(BaseModel):
    company_ko: str = None
    company_en: str = None
    company_ja: str = None
    tag_id: int = None

    class Config:
        orm_mode = True


class Tag(BaseModel):
    name_ko: str = None
    name_en: str = None
    name_ja: str = None

    class Config:
        orm_mode = True