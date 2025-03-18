from typing import Optional

from beanie import Document


class Projects(Document):
    name: str
    description: str
    frontend: Optional[str] = None
    backend: Optional[str] = None
    database: Optional[str] = None
    url: str
    github_repo: Optional[str] = None

    class Settings:
        name = "projects"
