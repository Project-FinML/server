import asyncio
from sqlalchemy import select
from app.core.db.session import SessionContext
from app.news.model.news import News

async def delete_news(id: int):
    async with SessionContext() as session:
        
        query = select(News).where(News.id == id)
        result = await session.execute(query)
        target_news = result.scalar_one_or_none()

        if target_news:
            await session.delete(target_news)
            await session.commit()
            print(f"{target_news.author}님의 데이터가 삭제되었습니다!")

        else:
            print(f"ID {id}번에 해당하는 뉴스가 없습니다.")

if __name__ == "__main__":
    asyncio.run(delete_news(1))