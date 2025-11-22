# models_sqlalchemy.py
from __future__ import annotations
from datetime import datetime, date
import os
from typing import Optional

from sqlalchemy import (
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
    Text,
    ForeignKey,
    create_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/dbname")


class Base(DeclarativeBase):
    pass


# 1 Users
class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    dob: Mapped[date] = mapped_column(DateTime, nullable=False)
    gender: Mapped[str] = mapped_column(String, nullable=False)
    nationality: Mapped[str] = mapped_column(String, nullable=False)

    target_weight: Mapped[float] = mapped_column(Float, nullable=False)
    target_duration: Mapped[int] = mapped_column(Integer, nullable=False)
    drinking_goal: Mapped[float] = mapped_column(Float, nullable=False)

    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    pin: Mapped[str] = mapped_column(String, nullable=False)
    is_pin_lock: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    pin_lock_datetime: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    occupation: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    income_value: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    companay_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    user_activity_level: Mapped[str] = mapped_column(String, nullable=False)
    exercise_frequency: Mapped[int] = mapped_column(Integer, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    last_active: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    tdee: Mapped[float] = mapped_column(Float, nullable=False)
    min_protein: Mapped[float] = mapped_column(Float, nullable=False)
    max_protein: Mapped[float] = mapped_column(Float, nullable=False)
    min_carb: Mapped[float] = mapped_column(Float, nullable=False)
    max_carb: Mapped[float] = mapped_column(Float, nullable=False)
    min_fat: Mapped[float] = mapped_column(Float, nullable=False)
    max_fat: Mapped[float] = mapped_column(Float, nullable=False)
    min_sugar: Mapped[float] = mapped_column(Float, nullable=False)
    max_sugar: Mapped[float] = mapped_column(Float, nullable=False)
    min_sodium: Mapped[float] = mapped_column(Float, nullable=False)
    max_sodium: Mapped[float] = mapped_column(Float, nullable=False)


# 2 MedicalHistories
class MedicalHistories(Base):
    __tablename__ = "medical_histories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    diesease_id: Mapped[int] = mapped_column(Integer, ForeignKey("diseases.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    start_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)


# 3 Diseases
class Diseases(Base):
    __tablename__ = "diseases"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)


# 4 EatingLifestyles
class EatingLifestyles(Base):
    __tablename__ = "eating_lifestyles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    lifestyle_id: Mapped[int] = mapped_column(Integer, ForeignKey("eating_lifestyle_categories.id"), nullable=False)
    start_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)


# 5 EatingLifestyleCategories
class EatingLifestyleCategories(Base):
    __tablename__ = "eating_lifestyle_categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)


# 6 UserAllergics (many-to-many)
class UserAllergics(Base):
    __tablename__ = "user_allergics"

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True)
    ingredient_id: Mapped[int] = mapped_column(Integer, ForeignKey("ingredients.id"), primary_key=True)


# 7 SocialPlatforms
class SocialPlatforms(Base):
    __tablename__ = "social_platforms"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)


# 8 UserSocialAccounts
class UserSocialAccounts(Base):
    __tablename__ = "user_social_accounts"

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True)
    platform_id: Mapped[int] = mapped_column(Integer, ForeignKey("social_platforms.id"), primary_key=True)
    connected_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)


# 9 UserStatistics
class UserStatistics(Base):
    __tablename__ = "user_statistics"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    height: Mapped[float] = mapped_column(Float, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    waist_size: Mapped[float] = mapped_column(Float, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)


# 10 Meals
class Meals(Base):
    __tablename__ = "meals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    meal_types_id: Mapped[int] = mapped_column(Integer, ForeignKey("meal_types.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    created_by: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    location: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("locations.id"), nullable=True)


# 11 MealTypes
class MealTypes(Base):
    __tablename__ = "meal_types"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)


# 12 Locations
class Locations(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    location_type: Mapped[str] = mapped_column(String, nullable=False)
    lat: Mapped[float] = mapped_column(Float, nullable=False)
    long: Mapped[float] = mapped_column(Float, nullable=False)


# 13 FoodMeals
class FoodMeals(Base):
    __tablename__ = "food_meals"

    meal_id: Mapped[int] = mapped_column(Integer, ForeignKey("meals.id"), primary_key=True)
    food_id: Mapped[int] = mapped_column(Integer, ForeignKey("foods.id"), primary_key=True)
    channel_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("channels.id"), nullable=True)
    price: Mapped[Optional[float]] = mapped_column(Float, nullable=True)


# 14 FavoriteFoods
class FavoriteFoods(Base):
    __tablename__ = "favorite_foods"

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True)
    food_id: Mapped[int] = mapped_column(Integer, ForeignKey("foods.id"), primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)


# 15 Foods
class Foods(Base):
    __tablename__ = "foods"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    category: Mapped[str] = mapped_column(String, nullable=False)
    carb: Mapped[float] = mapped_column(Float, nullable=False)
    protein: Mapped[float] = mapped_column(Float, nullable=False)
    fat: Mapped[float] = mapped_column(Float, nullable=False)
    sodium: Mapped[float] = mapped_column(Float, nullable=False)
    sugar: Mapped[float] = mapped_column(Float, nullable=False)
    kcal: Mapped[float] = mapped_column(Float, nullable=False)

    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_by: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)


# 16 Ingredients
class Ingredients(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)


# 17 Food_Ingredients
class Food_Ingredients(Base):
    __tablename__ = "food_ingredients"

    ingredient_id: Mapped[int] = mapped_column(Integer, ForeignKey("ingredients.id"), primary_key=True)
    food_id: Mapped[int] = mapped_column(Integer, ForeignKey("foods.id"), primary_key=True)

    amount: Mapped[float] = mapped_column(Float, nullable=False)
    unit: Mapped[str] = mapped_column(String, nullable=False)


# 18 Exercises
class Exercises(Base):
    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    exercise_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("exercise_types.id"), nullable=True)

    datetime: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    location: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("locations.id"), nullable=True)

    calories: Mapped[float] = mapped_column(Float, nullable=False)
    avg_heart_rate: Mapped[float] = mapped_column(Float, nullable=False)
    duration: Mapped[int] = mapped_column(Integer, nullable=False)


# 19 ExerciseTypes
class ExerciseTypes(Base):
    __tablename__ = "exercise_types"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)


# 20 MealPlans
class MealPlans(Base):
    __tablename__ = "meal_plans"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    type: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("meal_plan_types.id"), nullable=True)
    is_public: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    liked_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    created_by: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("users.id"), nullable=True)


# 21 MealPlanFoods
class MealPlanFoods(Base):
    __tablename__ = "meal_plan_foods"

    meal_plan_id: Mapped[int] = mapped_column(Integer, ForeignKey("meal_plans.id"), primary_key=True)
    food_id: Mapped[int] = mapped_column(Integer, ForeignKey("foods.id"), primary_key=True)


# 22 MealPlanTypes
class MealPlanTypes(Base):
    __tablename__ = "meal_plan_types"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)


# 23 FavoriteMealPlans
class FavoriteMealPlans(Base):
    __tablename__ = "favorite_meal_plans"

    meal_plan_id: Mapped[int] = mapped_column(Integer, ForeignKey("meal_plans.id"), primary_key=True)
    food_id: Mapped[int] = mapped_column(Integer, ForeignKey("foods.id"), primary_key=True)


# 24 Channels
class Channels(Base):
    __tablename__ = "channels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)


# 25 Drinkings
class Drinkings(Base):
    __tablename__ = "drinkings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    value: Mapped[float] = mapped_column(Float, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)


# --- Engine and Session ---
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
