"""Models for tags."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from trakr.models.base import BaseModel


class Tag(BaseModel):
    """Tag model for categorizing time entries."""

    name = Column(String(50), nullable=False)
    color = Column(String(7), nullable=True)  # Hex color code
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    # Changed backref to back_populates for consistency
    user = relationship("User", back_populates="tags")
    time_entries = relationship(
        "TimeEntry",
        secondary="time_entry_tag",
        back_populates="tags",
    )
