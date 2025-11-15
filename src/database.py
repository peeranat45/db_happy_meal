from datetime import datetime
import os
from sqlmodel import Field, Session, create_engine, select, SQLModel
from src.users.models import Users
from src.foods.models import FoodMeals, Foods, Meals, Channels, Regions, Ingredients, Food_Ingredients
from src.activities.models import Exercises, ExerciseTypes, UserStatistics
from src.models import Locations
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"), echo=True)
def init_db() -> None:
    print("init db")
    SQLModel.metadata.create_all(engine)