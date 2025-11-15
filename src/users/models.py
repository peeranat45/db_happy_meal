from sqlmodel import Field, SQLModel
from datetime import datetime

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

