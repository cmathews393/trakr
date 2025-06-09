"""Trakr Database Module and setup."""

import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = (
    os.environ.get("DATABASE_URL")
    or "postgresql+asyncpg://postgres:trakrpassword@localhost:5439/trakr"
)

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


async def get_db():
    """Dependency for getting async DB session."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
