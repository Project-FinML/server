import asyncio
from app.core.db.session import SessionContext
from app.news.model.news import News

async def insert_news(title: str, content: str, author: str):
    async with SessionContext() as session:
        new_post = News(
            title=title,
            content=content,
            author=author
        )
        
        session.add(new_post)
        
        await session.commit()
        print(f"{new_post.author}님의 데이터가 저장되었습니다!")

if __name__ == "__main__":
    asyncio.run(insert_news("두 번째 뉴스입니다", "SQLAlchemy와 MySQL을 연결했습니다.", "김철수"))