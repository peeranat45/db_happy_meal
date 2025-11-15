from sqlmodel import Field, SQLModel 
from datetime import datetime

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


