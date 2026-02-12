# main.py 또는 test_insert.py
import asyncio
from app.core.db.session import SessionContext
from app.news.model.news import News

async def insert_news():
    # 1. 세션 비서 소환
    async with SessionContext() as session:
        # 2. 데이터 객체 만들기 (여기서 드디어 "홍길동" 등장!)
        new_post = News(
            title="첫 번째 뉴스입니다",
            content="SQLAlchemy와 MySQL을 연결했습니다.",
            author="홍길동" 
        )
        
        # 3. 일꾼에게 데이터 전달
        session.add(new_post)
        
        # 4. DB에 최종 저장 (Commit)
        await session.commit()
        print(f"{new_post.author}님의 데이터가 저장되었습니다!")

if __name__ == "__main__":
    asyncio.run(insert_news())