import os
from sqlalchemy import (
    create_engine,
)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:1q2w3e4r@db.ujvbyqgnzdkiegkxqkzc.supabase.co:5432/postgres")
engine = create_engine(DATABASE_URL, echo=True)
