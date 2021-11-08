class ApiException(Exception):
    def __init__(self, code, message, extra=None):
        self.extra = extra
        self.code = code
        self.message = message



CREATE_COMPANY = "회사를 생성하였습니다."
CREATE_TAG = "TAG를 생성하였습니다."

INVALID_INPUT_COMPANY_NAME = "회사명이 입력되지 않았습니다"
INVALID_INPUT_TAG = "태그가 선택되지 않았습니다."
INVALID_INPUT_TAG_NAME = "태그명이 입력되지 않았습니다."

ALREADY_EXISTS_COMPANY_NAME = "이미 존재하는 회사명입니다."

CREATE_FAILED = "생성 실패"