from sqlalchemy import Column, Integer, String
from app.core.db.session import Base

class News(Base):
    __tablename__ = "news" # MySQL의 테이블 이름
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)   # 뉴스 제목
    content = Column(String(500))                 # 뉴스 내용
    author = Column(String(50))