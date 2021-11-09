
from dataclasses import dataclass, asdict
from os import path, environ

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


@dataclass
class Config:
    """
    기본 Configuration
    """
    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


@dataclass
class LocalConfig(Config):
    PROJ_RELOAD: bool = True
    DB_URL: str = "mysql+pymysql://root:poiu1234@localhost/wantedlab?charset=utf8mb4"


@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False


def conf():
    """
    환경 불러오기
    :return:
    """
    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "local"))



# SECRET_KEY = '^g!cb#jq-m-c5br7nb!lstsetk2!1$+*2*lr)+bnre4d=0djv!'
# ALGORITHM = 'HS256'
# DATABASE = {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'root',
#     'password': 'qwe123!!',
#     'database': 'wantedlab',
#     'charset': 'utf8mb4'
# }