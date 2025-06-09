"""Model file for association tables."""

from sqlalchemy import Column, ForeignKey, Integer

from trakr.models.base import BaseModel


class ProjectClient(BaseModel):
    """Association table between projects and clients."""

    __tablename__ = "project_client"
    project_id = Column(
        Integer,
        ForeignKey("project.id", ondelete="CASCADE"),
        primary_key=True,
    )
    client_id = Column(
        Integer,
        ForeignKey("client.id", ondelete="CASCADE"),
        primary_key=True,
    )


class TimeEntryTag(BaseModel):
    """Association table between time entries and tags."""

    __tablename__ = "time_entry_tag"
    time_entry_id = Column(
        Integer,
        ForeignKey("time_entry.id", ondelete="CASCADE"),
        primary_key=True,
    )
    tag_id = Column(Integer, ForeignKey("tag.id", ondelete="CASCADE"), primary_key=True)
