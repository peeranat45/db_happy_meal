from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

Base = declarative_base()

# Association tables
food_ingredients = Table('food_ingredients', Base.metadata,
    Column('food_id', Integer, ForeignKey('foods.id'), primary_key=True),
    Column('ingredients_id', Integer, ForeignKey('ingredients.id'), primary_key=True),
    Column('amount', Float, nullable=False),
    Column('unit', String, nullable=False)
)

food_meals = Table('food_meals', Base.metadata,
    Column('meal_id', Integer, ForeignKey('meals.id'), primary_key=True),
    Column('food_id', Integer, ForeignKey('foods.id'), primary_key=True),
    Column('channels_id', Integer, ForeignKey('channels.id')),
    Column('price', Float)
)

class MealType(Base):
    __tablename__ = 'meal_types'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class Food(Base):
    __tablename__ = 'foods'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    food_name = Column(String, nullable=False)
    food_category = Column(String, nullable=False)
    region_id = Column(Integer, ForeignKey('regions.id'))
    carb = Column(Float)
    protein = Column(Float)
    fat = Column(Float)
    sodium = Column(Float)
    sugar = Column(Float)
    kcal = Column(Float)
    is_deleted = Column(Boolean)
    created_by = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    creator = relationship("User", back_populates="foods_created")
    region = relationship("Region")
    ingredients = relationship("Ingredient", secondary=food_ingredients, back_populates="foods")
    meals = relationship("Meal", secondary=food_meals, back_populates="foods")
    favorite_foods = relationship("FavoriteFood", back_populates="food")

class Ingredient(Base):
    __tablename__ = 'ingredients'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    
    foods = relationship("Food", secondary=food_ingredients, back_populates="ingredients")

class Channel(Base):
    __tablename__ = 'channels'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)

class Meal(Base):
    __tablename__ = 'meals'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    meal_type = Column(Integer, ForeignKey('meal_types.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    created_by = Column(Integer, ForeignKey('users.id'), nullable=False)
    location = Column(Integer, ForeignKey('locations.id'))
    
    # Relationships
    creator = relationship("User", back_populates="meals_created")
    meal_type_rel = relationship("MealType")
    location_rel = relationship("Location")
    foods = relationship("Food", secondary=food_meals, back_populates="meals")

class FavoriteFood(Base):
    __tablename__ = 'favorite_foods'
    
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    food_id = Column(Integer, ForeignKey('foods.id'), primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    
    user = relationship("User", back_populates="favorite_foods")
    food = relationship("Food", back_populates="favorite_foods")