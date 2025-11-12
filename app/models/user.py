from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    dob = Column(DateTime(timezone=True), nullable=False)
    gender = Column(String, nullable=False)
    target_weight = Column(Float, nullable=False)
    drinking_goal = Column(Float, nullable=False)
    is_vegan = Column(Boolean)
    nationality = Column(String)
    occupation = Column(String)
    income_value = Column(Float)
    company_name = Column(String)
    user_activity_level = Column(String, nullable=False)
    exercise_frequency = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    last_active = Column(DateTime(timezone=True), nullable=False)
    
    # Relationships - simplify to avoid circular imports
    foods_created = relationship("Food", back_populates="creator")
    meals_created = relationship("Meal", back_populates="creator")
    drinkings = relationship("Drinking", back_populates="user")
    exercises = relationship("Exercise", back_populates="user")
    medical_histories = relationship("MedicalHistory", back_populates="user")
    favorite_foods = relationship("FavoriteFood", back_populates="user")
    social_accounts = relationship("UserSocialAccount", back_populates="user")
    statistics = relationship("UserStatistics", back_populates="user")
    created_meal_plans = relationship("MealPlan", back_populates="creator")
    # Remove the favorite_meal_plans relationship to avoid circular imports

class UserStatistics(Base):
    __tablename__ = 'user_statistics'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    height = Column(Float)
    weight = Column(Float)
    waist_size = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    user = relationship("User", back_populates="statistics")