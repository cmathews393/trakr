"""Models for clients and their relationshups."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from trakr.models.base import BaseModel


class Client(BaseModel):
    """Client model for grouping projects."""

    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=True)
    contact_name = Column(String(150), nullable=True)
    contact_phone = Column(String(50), nullable=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    # Changed backref to back_populates for consistency
    user = relationship("User", back_populates="clients")
    projects = relationship(
        "Project",
        secondary="project_client",
        back_populates="clients",
    )
