# [Assignment 3] Wantedlab  

## 팀원  
| **이름** | **Github Link** |
|:------|:-------------|
| 강대훈 | https://github.com/daehoon12 |
| 김훈태 | https://github.com/kim-hoontae |
| 안다민 | https://github.com/damin0320 |
| 이무현 | https://github.com/PeterLEEEEEE |
| 송빈호 | https://github.com/binogood |
| 정성헌 | https://github.com/Heon4856 | 


## 과제  안내

- 원티드 선호 기술스택: Python flask 또는 fastapi

> 다음과 같은 내용을 포함하는 테이블을 설계하고 다음과 같은 기능을 제공하는 REST API 서버를 개발해주세요.


### 데이터

- 회사 정보
    - 회사 이름 (다국어 지원 가능)
- 회사 정보 예제
    - 회사 이름 (원티드랩 / Wantedlab)
- 데이터 셋은 원티드에서 제공
- 데이터셋 예제
  - 원티드랩 회사는 한국어, 영어 회사명을 가지고 있습니다. (모든 회사가 모든 언어의 회사명을 가지고 있지는 않습니다.)
    
|컬럼명 | company_name_ko   | company_name_en | company_name_ja |
|-------|-------------------|-----------------|-----------------|
|내용   | 원티드랩          | wantedlab       |                 |

### REST API 기능

- 회사명 자동완성
    - 회사명의 일부만 들어가도 검색이 되어야 합니다.
- 회사 이름으로 회사 검색
- 새로운 회사 추가

### 개발 조건

- 제공되는 test case를 통과할 수 있도록 개발해야 합니다.
- ORM 사용해야 합니다.
- 결과는 JSON 형식이어야 합니다.
- database는 RDB를 사용해야 합니다.
- database table 갯수는 제한없습니다.
- 필요한 조건이 있다면 추가하셔도 좋습니다.
- Docker로 개발하면 가산점이 있습니다.


## 사용한 기술 스택

Back-end : <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;
<img alt="Python" src = "https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"/>&nbsp;
<img alt="Python" src = "https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/Docker-0052CC?style=for-the-badge&logo=Docker&logoColor=white"/>&nbsp;
<p>
Tool : <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/SWAGGER-5B8C04?style=for-the-badge&logo=Swagger&logoColor=white"/>
</p>

## 모델링  

![image](https://user-images.githubusercontent.com/78228444/140943226-817f8128-081b-4f94-80c4-001198350d00.png)

## 파일 구조  
- `./app`
  - `./database`    
    - `./__init__py`
    - `./conn.py`
    - `./schema.py`
  - `./model`
    - `./__init__py`
    - `./company_dao.py`
  - `./service`
    - `./__init__py`
    - `./company_service.py`
  - `./view`
    - `./__init__py`
    - `./company_view.py`
  - `./config.py`
  - `./main.py`
  - `./models.py`
  - `./response.py`
  - `./test_app.py`
  - `./run.py`
- `./migrations`
  - `./__init__py`
  - `./env.py`
- `./.gitignore`
- `./alembic.ini`
- `./requirements.txt`

## Endpoint  
![image](https://user-images.githubusercontent.com/78228444/140987466-18431ef6-5278-4cb6-a598-dfd439d9fd3d.png)


## 구현기능  

### 회사 생성(Company)
- ```회사생성 성공시``` :

```
- JSON
{
  "company_name": {
    "ko": "불4조",
    "en": "Phoneix",
    "ja": "タグタグ"
  },
  "tags": [
    {
      "tag_name": {
        "ko": "태그_1",
        "en": "tag_1",
        "ja": "タグ_1"
      }
    },
    {
      "tag_name": {
        "ko": "태그_12",
        "en": "tag_12",
        "ja": "タグ_12"
      }
    },
    {
      "tag_name": {
        "ko": "태그_14",
        "en": "tag_14",
        "ja": "タグ_14"
      }
    }
  ]
}headers=[("x-wanted-language", "ko")],

- 성공 메시지
- status_code : 200

{
  "company_name": {
    "company_name": "불4조"
  },
  "tags": [
    "태그_1",
    "태그_12",
    "태그_14"
  ]
}

- 새로운 언어 헤더에 입력시 언어 생성 후, 1 ~ 30번까지 새로운 언어 ID를 가진 tag를 생성 
  (어떤 언어가 들어올지 몰라 추가되는 모든 언어의 tag이름은 'tag_{idx}'로 구현하였습니다.')
  
- JSON
{
  "company_name": {
    "ko": "원티드",
    "en": "wanted",
    "fr": "프랑스"
  },
  "tags": [
    {
      "tag_name": {
        "ko": "태그_1",
        "en": "tag_1",
        "fr": "tag_1"
      }
    }
  ]
}

- 성공 메시지
- status_code : 200
{
  "company_name": "프랑스",
  "tags": [
    "tag_1"
  ]
}headers=[("x-wanted-language", "fr")]
```


- ```회사생성 실패시``` :

### 회사 조회 (Search)
- ```조회 성공시``` : status 200, header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.
```
{
  "company_name": "원티드랩",
  "tags": [
    "태그_4",
    "태그_16",
    "태그_20"
  ]
}
``` 

- ```조회 실패시``` : status 404, 
 ``` 
 '회사를 찾을수 없습니다.'
 ```

### 회사명 자동 완성 (Search)
- ```검색 성공시``` : status 200과 함께 쿼리와 언어값에 따른 모든 결과 값을 반환한다.
- ```검색 실패시``` : status 404와 함께 조건에 맞는 회사명이 없다는 에러 메시지를 반환한다.


### 아쉬웠던 점
Fastapi를 처음 다루다니보 문법에서 미숙한 부분이 많이 나타납니다.

처음에 할때는 "와 빠르고 편하다! Fastapi를 사용면 flask보다 빠른 api서버를 구성할 수 있겠다!"라는 마음가짐으로 도전 했습니다. 

경험해본결과 Fastapi는 확실히 flask랑 비교가 많이 되었습니다. asyncio를 사용할 수 있는점과 swagger를 지원해주는 부분에서 아주 좋았습니다.

코드를 짜면서 '미리 알았다면 더 좋았을텐데' 라는 많은 아쉬움이 담긴 코드를 작성했습니다.

실제로 기능은 다 구현하였으나 test_app.py를 실행시키면 하나가 실패로 나옵니다.

밤새 코드를 수정하는 부분에서 여러가지 문제가 발생하였고 결국은 프로젝트를 마무리하지 못하고 제출하게 되었습니다.

완성된 프로젝트를 제출하고 싶었지만 첫 Fastapi프로젝트로 무척 아쉬운 프로젝트로 남을 것 같습니다.

Fastapi는 충분히 매력적인 언어라고 생각이 들어 추후 프로젝트도 팀원들의 동의를 얻어 Fastapi로 해보고싶다는 생각이 들었습니다.

새벽까지 고생하신 팀원분들! 너무너무 고생하셨습니다.


# Reference
이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 원티드랩에서 출제한 과제를 기반으로 만들었습니다.
