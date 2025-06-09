"""Models for time tracking entries."""

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from trakr.models.base import BaseModel


class TimeEntry(BaseModel):
    """Time entry model for tracking time."""

    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(
        DateTime(timezone=True),
        nullable=True,
    )  # Null if timer is running
    description = Column(Text, nullable=True)
    is_running = Column(Boolean, default=False, nullable=False)

    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    project_id = Column(
        Integer,
        ForeignKey("project.id", ondelete="SET NULL"),
        nullable=True,
    )

    # Changed backref to back_populates for consistency
    user = relationship("User", back_populates="time_entries")
    project = relationship("Project", back_populates="time_entries")
    tags = relationship(
        "Tag",
        secondary="time_entry_tag",
        back_populates="time_entries",
    )
