# fastapi dev happy_meal_api.py
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlalchemy import Numeric, func

# # old DB
# DATABASE_URL = (
#     "postgresql://postgres.vjxkaznmielcwafxpbfm:1q2w3e4r"
#     "@aws-1-ap-southeast-1.pooler.supabase.com:6543/postgres"
# )


# new DB
DATABASE_URL = (
    "postgresql://postgres.ujvbyqgnzdkiegkxqkzc:1q2w3e4r"
    "@aws-1-ap-southeast-2.pooler.supabase.com:6543/postgres"
)

engine = create_engine(DATABASE_URL, echo=True)

# SQLModel table ----------------------------
class users(SQLModel, table=True):
    id: int = Field(primary_key=True)
    tdee: float | None = None
    max_protein: float | None = None
    max_carb: float | None = None
    max_fat: float | None = None

class meals(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str | None = None
    created_by: int = Field(foreign_key="users.id")
    created_at: datetime

class foods(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    category: str | None = None
    carb: float
    protein: float
    fat: float
    sodium: float
    sugar: float
    kcal: float
    is_deleted: bool
    created_by: int | None = None

class food_meals(SQLModel, table=True):
    meal_id: int = Field(foreign_key="meals.id", primary_key=True)
    food_id: int = Field(foreign_key="foods.id", primary_key=True)
    price: float | None = None
    channel_id: int | None = None

class Locations(SQLModel, table=True):
    __tablename__ = "locations"

    id: int = Field(primary_key=True)
    name: str | None = Field(default=None)
    location_type: str | None = Field(default=None)

class Exercise(SQLModel, table=True):
    __tablename__ = "exercises"  # make sure name matches your database

    id: int | None = Field(default=None, primary_key=True)
    name: str | None = Field(default=None)
    user_id: int | None = Field(default=None)
    exercise_type_id: int | None = Field(default=None)
    datetime: datetime | None
    location: str | None = Field(default=None)
    calories: float | None = Field(default=None)
    avg_heart_rate: int | None = Field(default=None)
    duration: int | None = Field(default=None)

class ExerciseType(SQLModel, table=True):
    __tablename__ = "exercise_types"

    id: int | None = Field(default=None, primary_key=True)
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)

class NutrientSummary(BaseModel):
    meal_date: str
    total_protein: float
    total_carb: float
    total_fat: float
    total_kcal: float
    max_protein: float
    max_carb: float
    max_fat: float
    daily_max_kcal: float
    remaining_kcal: float
    remaining_protein: float
    remaining_carb: float
    remaining_fat: float

# Request model for POST --------------------------------
class ExerciseCreate(BaseModel):
    name: str | None = None
    user_id: int | None = None
    exercise_type_id: int | None = None
    datetime: datetime | None
    location: str | None = None
    calories: float | None = None
    avg_heart_rate: int | None = None
    duration: int | None = None

class FoodCreate(BaseModel):
    name: str
    category: str | None = None
    carb: float
    protein: float
    fat: float
    sodium: float
    sugar: float
    kcal: float
    is_deleted: bool
    created_by: int | None = None

class MealCreate(BaseModel):
    meal_id: int | None = None
    food_id: int | None = None
    channel_id: int | None = None
    price: int | None = None

app = FastAPI()

# exercise ---------------------
@app.get("/exercises")
def get_exercises(user_id: int = Query(...), selected_date: datetime = Query(...)):
    start_datetime = datetime.combine(selected_date.date(), datetime.min.time())
    end_datetime = datetime.combine(selected_date.date(), datetime.max.time())
    # end_datetime = selected_date.date() + timedelta(days=30)

    with Session(engine) as session:
        # Join ExerciseType to get exercise_type name
        statement = (
            select(Exercise, ExerciseType.name, Locations.name)
            .join(ExerciseType, Exercise.exercise_type_id == ExerciseType.id)
            .join(Locations, Exercise.location == Locations.id)
            .where(Exercise.user_id == user_id)
            .where(Exercise.datetime >= start_datetime)
            .where(Exercise.datetime <= end_datetime)
        )

        results = session.exec(statement).all()


        if not results:
            raise HTTPException(status_code=404, detail="No data found")
        
        # Convert to list of dicts
        return [
            {
                "id": exercise.id,
                "name": exercise.name,
                "exercise_type": exercise_type_name,
                "location_name": locations_name,
                "duration": exercise.duration,
                "calories": exercise.calories,
                "avg_hr": exercise.avg_heart_rate,
                "date_time": exercise.datetime
            }
            for exercise, exercise_type_name, locations_name in results
        ]
    
@app.post("/exercises")
def create_exercise(data: ExerciseCreate):
    try:
        new_record = Exercise(**data.dict())

        with Session(engine) as session:
            session.add(new_record)
            session.commit()
            session.refresh(new_record)
            return "success"

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# meals ---------------------
@app.get("/meals")
async def get_meals(user_id: int, selected_date: datetime):

    start = datetime.combine(selected_date, datetime.min.time())
    end = datetime.combine(selected_date, datetime.max.time())

    with Session(engine) as session:

        stmt = (
            select(
                meals.id.label("meal_id"),
                meals.name.label("meal_name"),
                meals.created_at,
                foods.id.label("food_id"),
                foods.name,
                foods.category,
                foods.carb,
                foods.protein,
                foods.fat,
                foods.kcal,
                # food_meals.price,
                # food_meals.channels_id,
            )
            .join(food_meals, food_meals.meal_id == meals.id)
            .join(foods, foods.id == food_meals.food_id)
            .where(meals.created_by == user_id)
            .where(meals.created_at >= start)
            .where(meals.created_at <= end)
            .order_by(meals.created_at.asc(), foods.name.asc())
        )

        result = session.exec(stmt).all()

        if not result:
            raise HTTPException(status_code=404, detail="No data found")

        # SQLModel ส่งออก Row แบบ tuple → แปลงเป็น dict
        data = [row._asdict() for row in result]

        return data

@app.post("/meals")
def create_meals(meal_id: int, new_food: FoodCreate):
    try:
        with Session(engine) as session:

            new_record_food = foods(**new_food.dict())
            session.add(new_record_food)
            session.commit()
            session.refresh(new_record_food)  # new_record_food.id is now available

            new_link = food_meals(
                meal_id=meal_id,
                food_id=new_record_food.id
            )
            session.add(new_link)
            session.commit()
            session.refresh(new_link)

            return "success"

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# nutrient ---------------------
@app.get("/nutrient-summary", response_model=NutrientSummary)
async def read_nutrient_summary(user_id: int, date: str) -> NutrientSummary:
    try:
        meal_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

    try:
        with Session(engine) as session:
            stmt = (
                select(
                    func.date(meals.created_at).label("meal_date"),
                    func.round(func.sum(foods.protein).cast(Numeric), 2).label("total_protein"),
                    func.round(func.sum(foods.carb).cast(Numeric), 2).label("total_carb"),
                    func.round(func.sum(foods.fat).cast(Numeric), 2).label("total_fat"),
                    func.round(func.sum(foods.kcal).cast(Numeric), 2).label("total_kcal"),
                    func.round(users.max_protein.cast(Numeric), 2).label("max_protein"),
                    func.round(users.max_carb.cast(Numeric), 2).label("max_carb"),
                    func.round(users.max_fat.cast(Numeric), 2).label("max_fat"),
                    func.round(users.tdee.cast(Numeric), 2).label("daily_max_kcal"),
                    func.round((users.tdee - func.sum(foods.kcal)).cast(Numeric), 2).label("remaining_kcal"),
                    func.round((users.max_protein - func.sum(foods.protein)).cast(Numeric), 2).label("remaining_protein"),
                    func.round((users.max_carb - func.sum(foods.carb)).cast(Numeric), 2).label("remaining_carb"),
                    func.round((users.max_fat - func.sum(foods.fat)).cast(Numeric), 2).label("remaining_fat"),
                )
                .join(meals, meals.created_by == users.id)
                .join(food_meals, food_meals.meal_id == meals.id)
                .join(foods, foods.id == food_meals.food_id)
                .where(users.id == user_id)
                .where(func.date(meals.created_at) == meal_date)
                .group_by(
                    func.date(meals.created_at),
                    users.tdee,
                    users.max_protein,
                    users.max_carb,
                    users.max_fat,
                )
            )

            result = session.exec(stmt).mappings().first()

            if not result:
                raise HTTPException(status_code=404, detail="No data found")

            result_dict = dict(result)
            result_dict["meal_date"] = str(result_dict["meal_date"])

            return NutrientSummary(**result_dict)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query error: {str(e)}")