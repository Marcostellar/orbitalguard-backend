from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routes.waitlist import router as waitlist_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="OrbitalGuard AI API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # We'll tighten this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(waitlist_router)


@app.get("/")
def home():
    return {
        "project": "OrbitalGuard AI",
        "status": "Backend Online 🚀"
    }