from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

from app.models.share_base import Base

# Import the shared Base

load_dotenv()

# Build DATABASE_URL from environment variables
DB_HOST = os.getenv("HOST")
DB_USER = os.getenv("DB_USER")
DB_PORT = os.getenv("PORT")
DB_PASSWORD = os.getenv("PASSWORD")
DB_NAME = os.getenv("DATABASE_NAME", "postgres")

# Construct the database URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

print(f"Connecting to database: {DB_HOST}:{DB_PORT}")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    # Import all models to ensure they are registered with Base
    from app.models.user import User, UserStatistics
    from app.models.geographic import Location, Region
    from app.models.food import MealType, Food, Ingredient, Channel, Meal, FavoriteFood
    from app.models.activity import ExerciseType, Drinking, Exercise
    from app.models.health import Disease, MedicalHistory
    from app.models.social import SocialPlatform, UserSocialAccount
    from app.models.blog import BlogCategory, Blog
    from app.models.meal_plan import MealPlanType, MealPlan, FavoriteMealPlan, MealPlanFood
    
    Base.metadata.create_all(bind=engine)
    print("All tables created successfully!")