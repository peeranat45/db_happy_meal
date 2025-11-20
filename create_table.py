from datetime import datetime
import os
from sqlmodel import Field, Session, create_engine, select, SQLModel
from dotenv import load_dotenv

load_dotenv()

## Table List

class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    dob: datetime
    gender: str
    nationality: str

    target_weight: float
    drinking_goal: float
    is_vegan: bool
    user_activity_level: str
    exercise_frequency: int
    
    occupation: str | None = None
    income_value: float | None = None
    companay_name: str | None = None
    
    created_at: datetime
    last_active: datetime


class Meals(SQLModel, table=True):

    __tablename__ = "meals"

    id: int | None = Field(default=None, primary_key=True)
    name: str

    created_at: datetime
    created_by: int = Field(default=None, foreign_key="users.id")
    location: int | None = Field(default=None, foreign_key="locations.id")

class Foods(SQLModel, table=True):

    __tablename__ = "foods"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    category: str
    carb: float
    protein: float
    fat: float
    sodium: float
    sugar: float
    kcal: float

    created_by: int = Field(default=None, foreign_key="users.id")
    created_at: datetime

class FoodMeals(SQLModel, table=True):

    __tablename__ = "food_meals"

    meal_id: int = Field(default=None, foreign_key="meals.id", primary_key=True)
    food_id: int = Field(default=None, foreign_key="foods.id", primary_key=True)

    channel_id: int | None = Field(default=None, foreign_key="channels.id")
    price: float | None = Field(default=None)

class Channels(SQLModel, table=True):

    __tablename__ = "channels"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = Field(default=None)

class Regions(SQLModel, table=True):

    __tablename__ = "regions"

    id: int | None = Field(default=None, primary_key=True)
    region: str
    country: str | None = Field(default=None)


class Ingredients(SQLModel, table=True):

    __tablename__ = "ingredients"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    
    
class Food_Ingredients(SQLModel, table=True):
    
    __tablename__ = "food_ingredients"

    ingredient_id : int = Field(default=None, foreign_key="ingredient_id.id", primary_key=True)
    food_id : int = Field(default=None, foreign_key="food_id.id", primary_key=True)

    amount: float
    unit: str
    
class ExerciseTypes(SQLModel, table=True):

    __tablename__ = "exercise_types"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = Field(default=None)

class Exercises(SQLModel, table=True):

    __tablename__ = "exercises"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    user_id: int = Field(default=None, foreign_key="users.id")
    exercise_type_id: int | None = Field(default=None, foreign_key="exercise_types.id")

    datetime: datetime
    location: int | None = Field(default=None, foreign_key="locations.id")

    calories: float
    avg_heart_rate: float
    
class UserStatistics(SQLModel, table=True):

    __tablename__ = "user_statistics"


    id: int | None = Field(default=None, primary_key=True)
    height: float
    weight: float
    waist_size : float
    user_id: int = Field(default=None, foreign_key="users.id")
    created_at: datetime



engine = create_engine(os.getenv("DATABASE_URL"), echo=True)
def init_db() -> None:
    print("init db")
    SQLModel.metadata.create_all(engine)