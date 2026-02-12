# app/core/db/session.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. 실제 정보로 교체
DB_USER = "root"
DB_PASSWORD = "0515247934a!"  # image_09631e.png에서 입력한 것
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "article_db" # Workbench에서 방금 만든 이름

# 2. 비동기 주소 (mysql+aiomysql)
DATABASE_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 3. 엔진 및 세션 설정
engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()
AsyncSessionLocal = sessionmaker(
    bind=engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

# 4. 세션 비서 (Context Manager)
class SessionContext:
    def __init__(self):
        self.session = None
    async def __aenter__(self):
        self.session = AsyncSessionLocal()
        return self.session
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()