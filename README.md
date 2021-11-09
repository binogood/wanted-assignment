# [Assignment 3] Wantedlab  

## 배포주소
http://34.64.76.31
 
## API 문서주소
http://34.64.76.31/docs

## 사용한 기술 스택
<p>
<img alt="Python" src = "https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"/>
<img alt="Python" src = "https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white"/>
</p>

## 팀원  
| **이름** | **Github Link** |
|:------|:-------------|
| 강대훈 | https://github.com/daehoon12 |
| 김훈태 |https://github.com/kim-hoontae|
| 안다민| https://github.com/damin0320|
| 이무현 |https://github.com/PeterLEEEEEE |
| 송빈호 | https://github.com/binogood |
| 정성헌 | https://github.com/Heon4856 | 

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
- 회원가입 ```관리자 or 사용자```로 구분하여 구현하였습니다. 비밀번호는 ```bcrypt```를 이용해 암호화 시킨 뒤 db에 저장했습니다.  
- 로그인 시 DB에 이메일이 있는지 확인 후 ```bcrypt```을 이용해 DB에 저장되어 있는 암호와 비교한 뒤  ```jwt```를 이용해 토큰을 만들어 클라이언트에 보내게 하였습니다.  


### 회사명 검색 (Search)
- 공통으로 ```jwt```를 이용해 관리자 토큰이 있는지 확인하고 있으면 접근을 허락합니다. 인증이 안 됐을 시 403을 클라이언트에 보냅니다. 
- ```Create``` : Request 메시지로 아이디, 메뉴 이름, 메뉴 설명, 메뉴의 상품을 받습니다. 성공 시 Response로 201을 보내고 빠진 항목이 있거나 이미 존재하는 메뉴일 시 400을 클라이언트에 보냅니다.
- ```Update``` : 수정에 필요한 데이터를 Request 메시지를 보냅니다. Update가 성공 했을 때 서버는 받은 데이터를 Database에 반영한 뒤 200을 보냅니다. 업데이트가 실패 했을 경우 400을 클라이언트에 보냅니다.  
- ```Delete``` : 서버는 Menu Id를 Parameter인 Request 메시지를 받습니다. 받은 후 삭제에 성공하면 200, 실패 시 400을 클라이언트에 보냅니다.  
