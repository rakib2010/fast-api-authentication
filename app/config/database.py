from sqlalchemy.orm import declarative_base
from app.config.config import DATABASE_URL
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


Base = declarative_base()
engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
