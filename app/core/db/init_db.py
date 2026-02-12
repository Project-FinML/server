# init_db.py
import asyncio
from app.core.db.session import engine, Base
from app.news.model.news import News # 모델을 임포트해야 인식합니다.

async def init_models():
    async with engine.begin() as conn:
        # 이 명령어가 "News" 클래스를 SQL로 변환해 MySQL에 테이블을 만듭니다.
        await conn.run_sync(Base.metadata.create_all)
    print("테이블 생성 완료!")

if __name__ == "__main__":
    asyncio.run(init_models())