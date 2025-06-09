"""Setup base model for reuse."""

from sqlalchemy import Column, DateTime, Integer, func
from sqlalchemy.ext.declarative import declared_attr

from trakr.db import Base


class BaseModel(Base):
    """Base model class for all database models."""

    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    @declared_attr
    def __tablename__(self):  # noqa: ANN204
        """Table name based on class name."""
        return self.__name__.lower()
