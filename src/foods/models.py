from sqlmodel import Field, SQLModel
from datetime import datetime

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
    
