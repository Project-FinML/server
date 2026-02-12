from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_USER = "root"
DB_PASSWORD = "0515247934a!"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "article_db"

DATABASE_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL, echo=True) #통로
Base = declarative_base() #번역기

#비동기 세션 만들기
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession, 
    expire_on_commit=False
)

#세션 작동
class SessionContext:
    def __init__(self):
        self.session = None
    async def __aenter__(self):
        self.session = AsyncSessionLocal()
        return self.session
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()