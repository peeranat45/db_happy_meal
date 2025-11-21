from datetime import date, datetime
import os
from sqlmodel import Boolean, Field, Session, create_engine, select, SQLModel, table
from dotenv import load_dotenv

load_dotenv()

## Table List

## 1
class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    dob: datetime
    gender: str
    nationality: str

    target_weight: float
    target_duration: int
    drinking_goal: float

    email: str
    pin: str
    is_pin_lock: bool = False
    pin_lock_datetime: datetime | None = None
    occupation: str | None = None
    income_value: float | None = None
    companay_name: str | None = None

    user_activity_level: str
    exercise_frequency: int
    
    created_at: datetime
    last_active: datetime

    tdee: float
    min_protein: float
    max_protein: float
    min_carb: float
    max_carb: float
    min_fat: float
    max_fat: float
    min_sugar: float
    max_sugar: float
    min_sodium: float
    max_sodium: float


## 2
class MedicalHistories(SQLModel, table=True):
    __tablename__ = "medical_histories"
    
    id: int | None = Field(default=None, primary_key=True)
    diesease_id: int = Field(default=None, foreign_key="diseases.id")
    user_id: int = Field(default=None, foreign_key="users.id")
    start_date: datetime
    end_date: datetime | None = None

## 3
class Diseases(SQLModel, table=True):
    __tablename__ = "diseases"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = None

## 4
class EatingLifestyles(SQLModel, table=True):
    __tablename__ = "eating_lifestyles"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="users.id")
    lifestyle_id: int = Field(default=None, foreign_key="eating_lifestyle_categories.id")
    start_date: datetime
    end_date: datetime | None = None

## 5
class EatingLifestyleCategories(SQLModel, table=True):
    __tablename__ = "eating_lifestyle_categories"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = None

## 6
class UserAllergics(SQLModel, table=True):
    __tablename__ = "user_allergics"

    user_id: int = Field(default=None, foreign_key="users.id", primary_key=True)
    ingredient_id: int = Field(default=None, foreign_key="ingredients.id", primary_key=True)

## 7
class SocialPlatforms(SQLModel, table=True):
    __tablename__ = "social_platforms"

    id: int | None = Field(default=None, primary_key=True)
    name: str

## 8 
class UserSocialAccounts(SQLModel, table=True):
    __tablename__ = "user_social_accounts"
    user_id: int = Field(default=None, foreign_key="users.id", primary_key=True)
    platform_id: int = Field(default=None, foreign_key="social_platforms.id", primary_key=True)

    connected_at: datetime = datetime.now()

## 9
class UserStatistics(SQLModel, table=True):
    __tablename__ = "user_statistics"

    id: int | None = Field(default=None, primary_key=True)
    height: float
    weight: float
    waist_size : float
    user_id: int = Field(default=None, foreign_key="users.id")
    created_at: datetime

## 10
class Meals(SQLModel, table=True):

    __tablename__ = "meals"
    id: int | None = Field(default=None, primary_key=True)
    name: str
    meal_types_id: int = Field(default=None, foreign_key="meal_types.id")
    created_at: datetime = datetime.now()
    created_by: int = Field(default=None, foreign_key="users.id")
    location: int | None = Field(default=None, foreign_key="locations.id")

## 11
class MealTypes(SQLModel, table=True):
    __tablename__ = "meal_types"
    id: int | None = Field(default=None, primary_key=True)
    name: str

## 12
class Locations(SQLModel, table=True):
    __tablename__ = "locations"
    
    id: int | None = Field(default=None, primary_key=True)
    name: str
    location_type: str
    lat: float
    long: float

## 13
class FoodMeals(SQLModel, table=True):

    __tablename__ = "food_meals"

    meal_id: int = Field(default=None, foreign_key="meals.id", primary_key=True)
    food_id: int = Field(default=None, foreign_key="foods.id", primary_key=True)
    channel_id: int | None = Field(default=None, foreign_key="channels.id")
    price: float | None = Field(default=None)


## 14
class FavoriteFoods(SQLModel, table=True):
    __tablename__ = "favorite_foods"

    user_id: int = Field(default=None, foreign_key="users.id", primary_key=True)
    food_id: int = Field(default=None, foreign_key="foods.id", primary_key=True)
    created_at: datetime = datetime.now()

## 15
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

    is_deleted: bool = False
    created_by: int = Field(default=None, foreign_key="users.id")
    created_at: datetime = datetime.now()

## 16
class Ingredients(SQLModel, table=True):

    __tablename__ = "ingredients"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = None
    
## 17
class Food_Ingredients(SQLModel, table=True):
    
    __tablename__ = "food_ingredients"

    ingredient_id : int = Field(default=None, foreign_key="ingredient_id.id", primary_key=True)
    food_id : int = Field(default=None, foreign_key="food_id.id", primary_key=True)

    amount: float
    unit: str
    
## 18
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
    duration: int

## 19
class ExerciseTypes(SQLModel, table=True):

    __tablename__ = "exercise_types"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = Field(default=None)

## 20
class MealPlans(SQLModel, table=True):
    __tablename__ = "meal_plans"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = None
    type: int | None = Field(default=None, foreign_key="meal_plan_types.id") 
    is_public: bool = False
    liked_count: int = 0
    created_by: int | None = Field(default=None, foreign_key="users.id") 

## 21
class MealPlanFoods(SQLModel, table=True):
    __tablename__ = "meal_plan_foods"

    meal_plan_id: int = Field(default=None, foreign_key="meal_plans.id", primary_key=True) 
    food_id: int = Field(default=None, foreign_key="foods.id", primary_key=True) 

## 22
class MealPlanTypes(SQLModel, table=True):
    __tablename__ = "meal_plan_types"
    id: int | None = Field(default=None, primary_key=True)
    name: str

## 23
class FavoriteMealPlans(SQLModel, table=True):
    __tablename__ = "favorite_meal_plans"

    meal_plan_id: int = Field(default=None, foreign_key="meal_plans.id", primary_key=True) 
    food_id: int = Field(default=None, foreign_key="foods.id", primary_key=True)

## 24
class Channels(SQLModel, table=True):

    __tablename__ = "channels"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = Field(default=None)

## 25
class Drinkings(SQLModel, table=True):
    __tablename__ = "drinkings"

    id: int | None = Field(default=None, primary_key=True)

    value: float
    user_id: int = Field(default=None, foreign_key="users.id")
    created_at: datetime = datetime.now()


engine = create_engine(os.getenv("DATABASE_URL"), echo=True)
def init_db() -> None:
    print("init db")
    SQLModel.metadata.create_all(engine)

init_db()
    