# init_db.py
import asyncio
from app.core.db.session import engine, Base
from app.news.model.news import News # 모델을 임포트해야 인식합니다.

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all) # 기존 테이블 삭제
        # Base 메타데이터로 테이블 생성
        await conn.run_sync(Base.metadata.create_all)
    print("테이블 생성 완료!")

if __name__ == "__main__":
    asyncio.run(init_models())