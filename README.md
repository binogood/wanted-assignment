# [Assignment 3] Wantedlab  

## 배포주소
http://34.64.76.31
 
## API 문서주소
http://34.64.76.31/docs

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
![image](https://user-images.githubusercontent.com/32921115/140575249-e67b58be-d5c0-4bdf-baec-c265efcd898c.png)

## 구현기능  

### 회사 생성(Company), 태그 생성(Tag)
- ```회사생성 성공시``` :
- ```회사생성 실패시``` :
- ```태그생성 성공시``` :
- ```태그성공 실패시``` :


### 회사명 자동 완성 (Search)
- ```검색 성공시``` : status 200과 함께 쿼리와 언어값에 따른 모든 결과 값을 반환한다.
- ```검색 실패시``` : status 404와 함께 조건에 맞는 회사명이 없다는 에러 메시지를 반환한다.


### 회사명 검색 (Search)
- ```검색 성공시``` : 
- ```검색 실패시``` :

# Reference
이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 원티드랩에서 출제한 과제를 기반으로 만들었습니다.
