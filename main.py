from os import getenv

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import create_engine, SQLModel, Session, select

from models import ProjectModel


load_dotenv()

# Database setup
engine = create_engine(getenv("POSTGRES_DB_URL"))
SQLModel.metadata.create_all(engine)

app = FastAPI(
    title="Projects subdomain website",
    description="Website for projects.aguest.me domain",
    version="0.0.1",
)

# Middleware
app.add_middleware(
    CORSMiddleware,  # noqa
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Jinja2 templates setup
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Get the projects from the DB
    with Session(engine) as session:
        all_projects = session.exec(select(ProjectModel)).all()

    return templates.TemplateResponse(
        request=request, name="index.html", context={"projects": all_projects}
    )
