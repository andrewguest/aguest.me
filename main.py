from contextlib import asynccontextmanager

import motor.motor_asyncio

from beanie import init_beanie
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from models import Projects


load_dotenv()

# Jinja2 templates setup
templates = Jinja2Templates(directory="templates")


# Set up the MongoDB connection
async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb+srv://read-only-user:AtW8XtX2TU5sHy8p@aguestmecluster.3tbfk.mongodb.net/?retryWrites=true&w=majority&appName=AguestmeCluster"
    )
    await init_beanie(database=client.aguest_me, document_models=[Projects])


# Create the MongoDB database
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


# App setup
app = FastAPI(
    title="Projects subdomain website",
    description="Website for projects.aguest.me domain",
    version="0.0.1",
    lifespan=lifespan,
)

# Middleware
app.add_middleware(
    CORSMiddleware,  # noqa
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Get the projects from the DB
    all_projects = await Projects.find_all().to_list()
    print(all_projects)

    print(dir(Projects))

    return templates.TemplateResponse(
        request=request, name="index.html", context={"projects": all_projects}
    )
