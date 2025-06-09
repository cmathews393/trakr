"""User model for auth and ownership."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from trakr.models.base import BaseModel


class User(BaseModel):
    """User model for authentication and time entry ownership."""

    username = Column(String(100), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(150), nullable=True)
    is_active = Column(
        Integer,
        default=1,
        nullable=False,
    )

    # Relationship definitions
    projects = relationship(
        "Project", back_populates="user", cascade="all, delete-orphan"
    )
    clients = relationship(
        "Client", back_populates="user", cascade="all, delete-orphan"
    )
    time_entries = relationship(
        "TimeEntry", back_populates="user", cascade="all, delete-orphan"
    )
    tags = relationship("Tag", back_populates="user", cascade="all, delete-orphan")
