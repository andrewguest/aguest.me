from typing import Optional

from sqlmodel import Field, SQLModel


class ProjectModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    frontend: Optional[str] = None
    backend: Optional[str] = None
    database: Optional[str] = None
    url: str
    github_repo: Optional[str] = None
