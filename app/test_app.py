import pytest
import json
import requests

from fastapi.testclient import TestClient
from main import create_app


@pytest.fixture
def api():
    api = TestClient(create_app())
    return api

#
# def test_company_name_autocomplete(api):
#     """
#     1. 회사명 자동완성
#     회사명의 일부만 들어가도 검색이 되어야 합니다.
#     header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.
#     """
#     resp = api.get("/search?query=링크", headers=[("x-wanted-language", "ko")])
#     searched_companies = json.loads(resp.data.decode("utf-8"))
#
#     assert resp.status_code == 200
#     assert searched_companies == [
#         {"company_name": "주식회사 링크드코리아"},
#         {"company_name": "스피링크"},
#     ]


def test_company_name_autocomplete(api):
    """
    1. 회사명 자동완성
    회사명의 일부만 들어가도 검색이 되어야 합니다.
    header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.
    """
    resp = api.get("/search?query=링크", headers={"x-wanted-language": "ko"})
    # searched_companies = json.loads(resp.data.decode("utf-8"))

    assert resp.status_code == 200
    assert resp.json() == [
        {"company_name": "주식회사 링크드코리아"},
        {"company_name": "스피링크"},
    ]

    # # 검색된 회사가 없는경우 404를 리턴합니다.
    # resp = api.get(
    #     "/companies/없는회사", headers=[("x-wanted-language", "ko")]
    # )
    #
    # assert resp.status_code == 404


def test_new_company(api):
    """
    3.  새로운 회사 추가
    새로운 언어(tw)도 같이 추가 될 수 있습니다.
    저장 완료후 header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.
    """
    resp = api.post(
        "/companies",
        json={
            "company_name": {
                "ko": "라인 프레쉬",
                "tw": "LINE FRESH",
                "en": "LINE FRESH",
            },
            "tags": [
                {
                    "tag_name": {
                        "ko": "태그_1",
                        "tw": "tag_1",
                        "en": "tag_1",
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_8",
                        "tw": "tag_8",
                        "en": "tag_8",
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_15",
                        "tw": "tag_15",
                        "en": "tag_15",
                    }
                }
            ]
        },
        headers=[("x-wanted-language", "tw")],
    )

    company = json.loads(resp.data.decode("utf-8"))
    assert company == {
        "company_name": "LINE FRESH",
        "tags": [
            "tag_1",
            "tag_8",
            "tag_15",
        ],
    }
