from tracemalloc import start
from faker import Faker
import random
from datetime import datetime, timedelta, date
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from masterdata import EXERCISES_TYPE
from model import Drinkings, Exercises, Locations, SessionLocal, SocialPlatforms, UserSocialAccounts, UserStatistics, Users, Occupations, Meals, MealTypes, Foods, FoodMeals

DATABASE_URL = "postgresql://postgres.ujvbyqgnzdkiegkxqkzc:1q2w3e4r@aws-1-ap-southeast-2.pooler.supabase.com:6543/postgres"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

fake = Faker()

# --- Activity multiplier mapping ---
ACTIVITY_MULTIPLIERS = {
    "Sedentary": 1.2,
    "Lightly Active": 1.375,
    "Moderately Active": 1.55,
    "Very Active": 1.725,
    "Extremely Active": 1.9
}

def random_datetime_between(start: datetime, end: datetime):
    """Return random datetime between start and end."""
    delta_seconds = int((end - start).total_seconds())
    random_sec = random.randint(0, delta_seconds)
    return start + timedelta(seconds=random_sec)

# --- Helper functions ---
def get_occupation_ids(session: Session):
    return [occ.id for occ in session.query(Occupations).all()]

def get_meal_type_ids(session: Session):
    return [mt.id for mt in session.query(MealTypes).all()]

def get_food_ids(session: Session):
    return [f.id for f in session.query(Foods).all()]

# --- BMR and TDEE calculations ---
def calculate_bmr(gender: str, weight_kg: float, height_cm: float, age: int) -> float:
    if gender.lower() == "male":
        return 66 + (13.7 * weight_kg) + (5 * height_cm) - (6.8 * age)
    else:
        return 655 + (9.6 * weight_kg) + (1.8 * height_cm) - (4.7 * age)

def calculate_tdee(bmr: float, activity_level: str) -> float:
    multiplier = ACTIVITY_MULTIPLIERS.get(activity_level, 1.2)
    return bmr * multiplier

def daily_calorie_adjustment(current_weight: float, goal_weight: float, duration_days: int) -> float:
    kcal_per_kg = 7700
    return (current_weight - goal_weight) * kcal_per_kg / duration_days

def calculate_macros(tdee: float):
    min_protein = round(tdee * 0.1 / 4, 1)
    max_protein = round(tdee * 0.2 / 4, 1)
    min_carb = round(tdee * 0.45 / 4, 1)
    max_carb = round(tdee * 0.65 / 4, 1)
    min_fat = round(tdee * 0.2 / 9, 1)
    max_fat = round(tdee * 0.35 / 9, 1)
    min_sugar = round(min_carb * 0.1, 1)
    max_sugar = round(max_carb * 0.15, 1)
    min_sodium = 1500
    max_sodium = 2500
    return min_protein, max_protein, min_carb, max_carb, min_fat, max_fat, min_sugar, max_sugar, min_sodium, max_sodium

# --- Generate a single user ---
def generate_user(session: Session):
    occupation_ids = get_occupation_ids(session)

    # --- Basic info ---
    first_name = fake.first_name()
    last_name = fake.last_name()
    dob = fake.date_of_birth(minimum_age=18, maximum_age=65)
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    gender = random.choice(["Male", "Female"])
    nationality = fake.country()

    # --- Height based on gender ---
    if gender == "Male":
        height = round(random.uniform(160, 190), 1)
    else:
        height = round(random.uniform(150, 175), 1)
    height_m = height / 100

    # --- BMI categories for realistic weight ---
    bmi_categories = {
        "Underweight": (14, 18.4),
        "Healthy": (18.5, 24.9),
        "Overweight": (25, 29.9),
        "Obese": (30, 40)
    }

    category = random.choices(
        population=list(bmi_categories.keys()),
        weights=[0.05, 0.6, 0.25, 0.1],
        k=1
    )[0]

    min_bmi, max_bmi = bmi_categories[category]
    weight = round(random.uniform(min_bmi * height_m ** 2, max_bmi * height_m ** 2), 1)

    print(f"Users Start Weight = {weight}, height = {height}")

    # --- Waist size based on gender and BMI category ---
    waist_ratios = {
        "Male": {
            "Underweight": (0.38, 0.42),
            "Healthy": (0.43, 0.48),
            "Overweight": (0.49, 0.55),
            "Obese": (0.56, 0.65)
        },
        "Female": {
            "Underweight": (0.35, 0.39),
            "Healthy": (0.40, 0.45),
            "Overweight": (0.46, 0.52),
            "Obese": (0.53, 0.60)
        }
    }
    ratio_min, ratio_max = waist_ratios[gender][category]
    waist_size = round(height * random.uniform(ratio_min, ratio_max), 1)

    # --- Target weight and duration ---
    target_weight = round(random.uniform(45, weight), 1)
    target_duration = random.randint(30, 180)

    # --- TDEE and macros ---
    activity_level = random.choice(list(ACTIVITY_MULTIPLIERS.keys()))
    bmr = calculate_bmr(gender, weight, height, age)
    tdee = calculate_tdee(bmr, activity_level)
    daily_adjustment = daily_calorie_adjustment(weight, target_weight, target_duration)
    recommended_calories = tdee - daily_adjustment
    min_protein, max_protein, min_carb, max_carb, min_fat, max_fat, min_sugar, max_sugar, min_sodium, max_sodium = calculate_macros(tdee)

    # --- Other info ---
    drinking_goal = round(random.uniform(1, 3), 1)
    email = fake.unique.email()
    pin = str(fake.random_number(digits=6, fix_len=True))
    is_pin_lock = random.choice([True, False])

    # User created_at between 2025-01-01 and now
    start_date = datetime(2025, 9, 1)
    end_date_random = datetime(2025, 11, 1)
    end_date = datetime.utcnow()
    created_at = random_datetime_between(start_date, end_date_random)
    pin_lock_datetime = random_datetime_between(created_at, end_date) if is_pin_lock else None
    last_active = random_datetime_between(created_at, end_date)

    occupation_id = random.choice(occupation_ids)
    income_value = round(random.uniform(20000, 200000), 2)
    company_name = fake.company()
    exercise_frequency = random.randint(0, 7)

    user = Users(
        first_name=first_name,
        last_name=last_name,
        dob=dob,
        gender=gender,
        nationality=nationality,
        target_weight=target_weight,
        target_duration=target_duration,
        drinking_goal=drinking_goal,
        email=email,
        pin=pin,
        is_pin_lock=is_pin_lock,
        pin_lock_datetime=pin_lock_datetime,
        occupation_id=occupation_id,
        income_value=income_value,
        companay_name=company_name,
        user_activity_level=activity_level,
        exercise_frequency=exercise_frequency,
        tdee=round(tdee, 1),
        min_protein=min_protein,
        max_protein=max_protein,
        min_carb=min_carb,
        max_carb=max_carb,
        min_fat=min_fat,
        max_fat=max_fat,
        min_sugar=min_sugar,
        max_sugar=max_sugar,
        min_sodium=min_sodium,
        max_sodium=max_sodium,
        created_at=created_at,
        last_active=last_active
    )

    return user, height, weight, waist_size, activity_level


# --- Generate meals for a user ---
def generate_meals(session: Session, user_id: int, user_created_at: datetime, max_meals_per_day: int = 3):
    meal_type_ids = get_meal_type_ids(session)
    food_ids = get_food_ids(session)
    end_date = datetime.utcnow()
    
    current_day = user_created_at.date()
    last_day = end_date.date()

    while current_day <= last_day:
        # Random number of meals for this day
        num_meals = random.randint(1, max_meals_per_day)
        for _ in range(num_meals):
            meal_name = f"{fake.word().capitalize()} Meal"
            meal_type_id = random.choice(meal_type_ids)
            # Random time during the day
            meal_datetime = datetime.combine(current_day, datetime.min.time()) + timedelta(
                seconds=random.randint(0, 86399)
            )
            meal = Meals(
                name=meal_name,
                meal_types_id=meal_type_id,
                created_at=meal_datetime,
                created_by=user_id,
            )
            session.add(meal)
            session.flush()  # get meal.id

            # Assign 2-5 random foods
            num_foods = random.randint(2, 5)
            selected_food_ids = random.sample(food_ids, num_foods)
            for food_id in selected_food_ids:
                price = round(random.uniform(30, 500), 2)
                channel_id = None
                food_meal = FoodMeals(
                    meal_id=meal.id,
                    food_id=food_id,
                    channel_id=channel_id,
                    price=price
                )
                session.add(food_meal)
        
        current_day += timedelta(days=1)

def generate_user_statistics(
    session: Session, 
    user_id: int, 
    user_created_at: datetime, 
    start_weight: float, 
    start_height: float, 
    start_waist: float,
    activity_level: int
):
    """
    Generate daily UserStatistics with realistic weight-change patterns.
    """

    end_date = datetime.utcnow().date()
    current_day = user_created_at.date()

    # Starting values
    weight = start_weight
    waist = start_waist
    height = start_height

    # ----- Assign Weight Change Scenario -----
    # 1 = steady decrease, 2 = steady increase, 3 = stable, 4 = yo-yo
    scenario = random.choice([1, 2, 3, 4])

    while current_day <= end_date:

        # ----- SCENARIO LOGIC -----
        if activity_level == "Extremely Active" or "Very Active":  
            # Steady decrease (dieting)
            daily_weight_change = random.uniform(-0.15, -0.05)
            daily_waist_change = random.uniform(-0.12, -0.05)

        elif scenario == "Sedentary":
            # Steady increase (bulking)
            daily_weight_change = random.uniform(0.05, 0.15)
            daily_waist_change = random.uniform(0.05, 0.12)

        elif scenario == "Lightly Active":
            # Stable weight (maintenance)
            daily_weight_change = random.uniform(-0.05, 0.05)
            daily_waist_change = random.uniform(-0.05, 0.05)

        elif scenario == "Sedentary":
            # Yo-yo effect (2–4 week cycles)
            cycle_length = 14  # 2 weeks up, 2 weeks down
            cycle_position = (current_day - user_created_at.date()).days % (cycle_length * 2)

            if cycle_position < cycle_length:
                # Losing phase
                daily_weight_change = random.uniform(-0.12, -0.03)
                daily_waist_change = random.uniform(-0.10, -0.03)
            else:
                # Gaining phase
                daily_weight_change = random.uniform(0.03, 0.12)
                daily_waist_change = random.uniform(0.03, 0.10)
                

        # Apply changes
        weight += round(daily_weight_change, 3)
        waist += round(daily_waist_change, 3)

        # Prevent unrealistic values
        weight = max(35, min(weight, 200))
        waist = max(40, min(waist, 200))

        created_at = datetime.combine(
            current_day, 
            datetime.min.time()
        ) + timedelta(seconds=random.randint(0, 86399))

        # Insert statistics
        stat = UserStatistics(
            user_id=user_id,
            height=height,
            weight=round(weight, 1),
            waist_size=round(waist, 1),
            created_at=created_at
        )

        session.add(stat)
        current_day += timedelta(days=1)


def get_exercise_type_info(session: Session):
    """
    Returns a list of exercise types as:
    [
        {"id": 1, "name": "Running"},
        {"id": 2, "name": "Cycling"},
        ...
    ]
    """
    rows = session.execute(text("SELECT id, name FROM exercise_types")).fetchall()
    return [{"id": r[0], "name": r[1]} for r in rows]


def generate_exercises(session: Session, user_id: int, user_created_at: datetime, activity_level: str):
    """
    Generate realistic daily exercise logs for the user.
    NOW uses DB exercise_type table: id + name.
    """

    # ---- Load exercise types from DB ----
    exercise_types = get_exercise_type_info(session)
    exercise_names = [e["name"] for e in exercise_types]

    # ---- Weekly profile per activity level ----
    profiles = {
        "Sedentary":            {"days_per_week": (0, 1), "base_hr": (85, 110),  "base_kcal": (60, 150)},
        "Lightly Active":       {"days_per_week": (1, 2), "base_hr": (90, 120),  "base_kcal": (100, 250)},
        "Moderately Active":    {"days_per_week": (2, 4), "base_hr": (100, 135), "base_kcal": (150, 400)},
        "Very Active":          {"days_per_week": (4, 6), "base_hr": (115, 150), "base_kcal": (250, 700)},
        "Extremely Active":     {"days_per_week": (5, 7), "base_hr": (130, 170), "base_kcal": (400, 1200)}
    }
    profile = profiles.get(activity_level, profiles["Sedentary"])

    # ---- Intensity mapping ----
    intensity_map = {
        "Running": "high",
        "Cycling": "medium",
        "Swimming": "high",
        "HIIT": "high",
        "Jump Rope": "high",
        "Boxing": "high",
        "CrossFit": "high",
        "Weight Training": "medium",
        "Martial Arts": "high",
        "Climbing": "high",
        "Rowing": "medium",
        "Skiing": "medium",
        "Surfing": "medium",
        "Jumping Jacks": "medium",
        "Burpees": "high",
        "Mountain Climbers": "high",
        "Dance Fitness": "medium",
        "Zumba": "medium",
        "Aerobics": "medium",
        "Hiking": "medium",
        "Skating": "medium",
        "Yoga": "low",
        "Pilates": "low",
        "Stretching": "low",
        "Walking": "low",
        "Tai Chi": "low",
        "Bodyweight Training": "medium",
        "Plank": "low",
        "Lunges": "medium",
        "Squats": "medium"
    }

    intensity_factor = {"low": 0.8, "medium": 1.0, "high": 1.2}

    # ---- Date range ----
    start_date = user_created_at.date()
    end_date = datetime.utcnow().date()
    current_date = start_date

    # ---- Weekly exercise pattern ----
    weekly_plan_days = random.randint(*profile["days_per_week"])

    while current_date <= end_date:

        # Should user exercise today?
        exercise_today = random.random() < (weekly_plan_days / 7)

        if exercise_today:
            # Pick a random exercise from DB
            chosen = random.choice(exercise_types)
            exercise_name = chosen["name"]
            exercise_type_id = chosen["id"]

            # Intensity
            intensity = intensity_map.get(exercise_name, "medium")

            # Duration
            if intensity == "low":
                duration = random.randint(15, 40)
            elif intensity == "medium":
                duration = random.randint(25, 60)
            else:
                duration = random.randint(20, 45)

            # Calories burned
            base_min, base_max = profile["base_kcal"]
            calories = random.uniform(base_min, base_max) * intensity_factor[intensity]

            # Heart rate
            hr_min, hr_max = profile["base_hr"]
            avg_hr = random.uniform(hr_min, hr_max) * intensity_factor[intensity]

            # Random time in the day
            exercise_datetime = datetime.combine(
                current_date,
                datetime.min.time()
            ) + timedelta(seconds=random.randint(0, 86399))

            # Save record
            exercise = Exercises(
                name=exercise_name,
                user_id=user_id,
                exercise_type_id=exercise_type_id,  # updated
                datetime=exercise_datetime,
                location=None,
                calories=round(calories, 1),
                avg_heart_rate=round(avg_hr, 1),
                duration=duration
            )

            session.add(exercise)

        current_date += timedelta(days=1)


def generate_drinkings(session: Session, user_id: int, user_created_at: datetime, drinking_goal: float):
    """
    Generate multiple drinking records per day from user_created_at to today.
    Daily total is based on user's drinking_goal with below/average/above variations.
    Each day has 2–6 drinking events spread randomly across the day.
    """
    today = datetime.utcnow().date()
    current_day = user_created_at.date()

    while current_day <= today:
        # Decide scenario: below / average / above total for the day
        scenario = random.random()

        if scenario < 0.30:  # 30% below goal
            daily_total = random.uniform(drinking_goal * 0.4, drinking_goal * 0.8)
        elif scenario < 0.70:  # 40% average
            daily_total = random.uniform(drinking_goal * 0.8, drinking_goal * 1.2)
        else:  # 30% above
            daily_total = random.uniform(drinking_goal * 1.2, drinking_goal * 1.6)

        # Decide how many drinking sessions today (like hydration logs)
        sessions = random.randint(2, 6)

        # Split daily total into 'sessions' random parts
        # Generate random weights to distribute total fairly
        weights = [random.random() for _ in range(sessions)]
        weight_sum = sum(weights)
        portions = [(w / weight_sum) * daily_total for w in weights]

        # Create individual drinking entries
        for portion in portions:
            created_at = (
                datetime.combine(current_day, datetime.min.time()) +
                timedelta(seconds=random.randint(0, 86399))
            )

            record = Drinkings(
                user_id=user_id,
                value=round(portion, 2),
                created_at=created_at
            )
            session.add(record)

        current_day += timedelta(days=1)


def generate_user_social_accounts(session: Session, user, max_platforms: int = 4):
    """
    Generate random social media accounts for a user.
    - Uses existing social_platforms table.
    - User may have 0–3 platforms.
    - Skips platforms already linked.
    """

    # Get all platform IDs
    platforms = session.query(SocialPlatforms).all()
    platform_ids = [p.id for p in platforms]

    if not platform_ids:
        print("No social platforms found. Skipping social account generation.")
        return

    # Existing user social accounts
    existing = (
        session.query(UserSocialAccounts.platform_id)
        .filter(UserSocialAccounts.user_id == user.id)
        .all()
    )
    existing_platforms = {row[0] for row in existing}

    # How many platforms this user will have?
    num_accounts = random.randint(0, max_platforms)

    # Available platforms not yet used
    available = list(set(platform_ids) - existing_platforms)

    if not available:
        return  # user already has all platforms

    # Randomly pick platforms for this user
    chosen_platforms = random.sample(available, min(num_accounts, len(available)))

    for platform_id in chosen_platforms:

        connected_at = fake.date_time_between(
            start_date=user.created_at,
            end_date=datetime.utcnow()
        )

        account = UserSocialAccounts(
            user_id=user.id,
            platform_id=platform_id,
            connected_at=connected_at
        )

        session.add(account)


# --- Generate multiple users along with meals ---
def generate_users(n: int):
    session = SessionLocal()
    users_list = []

    for _ in range(n):
        user, height, weight, waist_size, activity_level = generate_user(session)
        session.add(user)
        session.flush()  # to get user.id

        # Create meals and food_meals for this user
        generate_meals(session, user.id, user.created_at, max_meals_per_day=4)
        generate_user_statistics(
            session=session,
            user_id=user.id,
            user_created_at=user.created_at,
            start_height=height,
            start_weight=weight,
            start_waist=waist_size,
            activity_level=activity_level
        )

        generate_exercises(
            session=session,
            user_id=user.id,
            user_created_at=user.created_at,
            activity_level=activity_level
        )

        # Drinking
        generate_drinkings(
            session=session,
            user_id=user.id,
            user_created_at=user.created_at,
            drinking_goal=user.drinking_goal,
        )

        # Social Media
        generate_user_social_accounts(session, user)



        users_list.append(user)

    session.commit()
    session.close()
    print(f"{n} users with meals generated successfully.")






# Example usage
generate_users(1)
