from datetime import datetime
from pydantic import BaseModel

from src.schemas import BaseResponse

class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    dob: datetime
    gender: str
    nationality: str
    email: str | None = None

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

class CreateUserResponse(BaseResponse):
    pass
    

class UserProfileResponse(BaseResponse):
    first_name: str
    last_name: str
    dob: datetime
    gender: str
    nationality: str
    email: str | None = None

    occupation: str | None = None
    income_value: float | None = None
    companay_name: str | None = None