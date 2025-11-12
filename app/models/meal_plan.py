from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

Base = declarative_base()

class MealPlanType(Base):
    __tablename__ = 'meal_plan_types'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class MealPlan(Base):
    __tablename__ = 'meal_plans'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    type = Column(Integer, ForeignKey('meal_plan_types.id'))
    created_at = Column(DateTime, server_default=func.now())
    created_by = Column(Integer, ForeignKey('users.id'), nullable=False)
    is_public = Column(Boolean)
    used_count = Column(Integer)
    
    # Remove complex relationships for now
    creator = relationship("User")
    plan_type = relationship("MealPlanType")

class FavoriteMealPlan(Base):
    __tablename__ = 'favorite_meal_plans'
    
    meal_plan_id = Column(Integer, ForeignKey('meal_plans.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    
    meal_plan = relationship("MealPlan")
    user = relationship("User")

class MealPlanFood(Base):
    __tablename__ = 'meal_plan_foods'
    
    meal_plan_id = Column(Integer, ForeignKey('meal_plans.id'), primary_key=True)
    food_id = Column(Integer, ForeignKey('foods.id'), primary_key=True)
    
    meal_plan = relationship("MealPlan")
    food = relationship("Food")