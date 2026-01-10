from fastapi import FastAPI
from api.routes.health_api import router as health_router
from api.routes.ingest_api import router as ingest_router

app = FastAPI(title="Domain Engine API")

app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(ingest_router, prefix="/ingest", tags=["ingest"])
