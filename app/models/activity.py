from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

Base = declarative_base()

class ExerciseType(Base):
    __tablename__ = 'excercise_types'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

class Drinking(Base):
    __tablename__ = 'drinkings'
    
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime, nullable=False)
    value = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    user = relationship("User", back_populates="drinkings")

class Exercise(Base):
    __tablename__ = 'excercise'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    exercise_type_id = Column(Integer, ForeignKey('excercise_types.id'), nullable=False)
    date_time = Column(DateTime, server_default=func.now())
    location = Column(Integer, ForeignKey('locations.id'))
    calories = Column(Float, nullable=False)
    avg_heart_rate = Column(Float, nullable=False)
    
    user = relationship("User", back_populates="exercises")
    exercise_type = relationship("ExerciseType")
    location_rel = relationship("Location")