import asyncio
from app.core.db.session import SessionContext
from app.news.model.news import News

async def insert_news():
    async with SessionContext() as session:
        new_post = News(
            title="첫 번째 뉴스입니다",
            content="SQLAlchemy와 MySQL을 연결했습니다.",
            author="홍길동" 
        )
        
        session.add(new_post)
        
        await session.commit()
        print(f"{new_post.author}님의 데이터가 저장되었습니다!")

if __name__ == "__main__":
    asyncio.run(insert_news())