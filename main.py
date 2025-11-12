from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager
import uvicorn

from app.database.database import create_tables, get_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup - this is synchronous now
    create_tables()
    print("Database tables created successfully!")
    yield
    print("Application shutting down...")

app = FastAPI(
    title="Health & Nutrition API",
    description="A comprehensive health, nutrition, and fitness tracking API",
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/")
async def root():
    return {"message": "Health & Nutrition API is running!"}

@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected",
            "message": "Successfully connected to Supabase PostgreSQL"
        }
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Database connection failed: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)