"""Models for managing projects."""

from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from trakr.models.base import BaseModel


class Project(BaseModel):
    """Project model for grouping time entries."""

    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    color = Column(String(7), nullable=True)  # Hex code for project color
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    # Changed backref to back_populates for consistency
    user = relationship("User", back_populates="projects")
    time_entries = relationship(
        "TimeEntry",
        back_populates="project",
        cascade="all, delete-orphan",
    )
    clients = relationship(
        "Client",
        secondary="project_client",
        back_populates="projects",
    )
