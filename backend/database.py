from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 本地数据库文件，会自动生成在 backend 目录下
SQLALCHEMY_DATABASE_URL = "sqlite:///./director.db"

# 创建引擎
# connect_args={"check_same_thread": False} 仅用于 SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 声明基类
Base = declarative_base()

# 获取数据库会话的依赖函数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()