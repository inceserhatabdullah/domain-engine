from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.v1.ingest import router as ingest_router

app = FastAPI(title="Domain Engine API")

app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(ingest_router, prefix="/v1/ingest", tags=["ingest"])
