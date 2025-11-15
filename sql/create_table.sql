-- Create tables in dependency order

-- 1. Independent tables (no foreign keys)
CREATE TABLE social_platforms (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE blog_categories (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE meal_types (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE excercise_types (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL 
);

CREATE TABLE meal_plan_types (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE diseases (
    id SERIAL PRIMARY KEY,
    disease_name TEXT NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE channels (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE regions (
    id SERIAL PRIMARY KEY,
    country TEXT,
    subRegion TEXT,
    region TEXT NOT NULL
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    lat REAL,
    long REAL
);

CREATE TABLE ingredients (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL
);

-- 2. Users table (independent)
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    dob TIMESTAMP WITH TIME ZONE NOT NULL,
    gender TEXT NOT NULL,
    target_weight REAL NOT NULL,
    drinking_goal REAL NOT NULL,
    is_vegan boolean NULL,
    nationality TEXT NULL,
    occupation TEXT NULL,
    income_value REAL NULL,
    company_name TEXT NULL,
    user_activity_level TEXT NOT NULL,
    exercise_frequency REAL NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    last_active TIMESTAMP WITH TIME ZONE NOT NULL
);

-- 3. Tables that depend on users and other basic tables
CREATE TABLE foods (
    id SERIAL PRIMARY KEY,
    food_name TEXT NOT NULL,
    food_category TEXT NOT NULL,
    region_id INTEGER,
    carb REAL,
    protein REAL,
    fat REAL,
    sodium REAL,
    sugar REAL,
    kcal REAL,
    is_deleted BOOLEAN,
    created_by INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES users(id),
    FOREIGN KEY (region_id) REFERENCES regions(id)
);

CREATE TABLE blogs (
    id SERIAL PRIMARY KEY,
    blog_name TEXT NOT NULL,
    content TEXT NOT NULL,
    published_at DATE,
    views INTEGER,
    likes INTEGER
);

CREATE TABLE meal_plans (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    type INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by INTEGER NOT NULL,
    is_public BOOLEAN,
    used_count INTEGER,
    FOREIGN KEY (type) REFERENCES meal_plan_types(id),
    FOREIGN KEY (created_by) REFERENCES users(id)
);

-- 4. Junction tables and tables with multiple dependencies
CREATE TABLE user_social_accounts (
    user_id INTEGER NOT NULL,
    platform_id  INTEGER NOT NULL,
    connected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (platform_id) REFERENCES social_platforms(id)
);

CREATE TABLE food_ingredients (
    food_id INTEGER NOT NULL,
    ingredients_id INTEGER,
    amount REAL NOT NULL,
    unit TEXT NOT NULL,
    FOREIGN KEY (food_id) REFERENCES foods (id),
    FOREIGN KEY (ingredients_id) REFERENCES ingredients (id)
);

CREATE TABLE meals (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    meal_type INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_by INTEGER NOT NULL,
    location INTEGER,
    FOREIGN KEY (created_by) REFERENCES users (id),
    FOREIGN KEY (location) REFERENCES locations (id),
    FOREIGN KEY (meal_type) REFERENCES meal_types (id)
);

CREATE TABLE food_meals (
    meal_id INTEGER NOT NULL,
    food_id INTEGER NOT NULL,
    channels_id INTEGER,
    price REAL,
    FOREIGN KEY (meal_id) REFERENCES meals (id),
    FOREIGN KEY (food_id) REFERENCES foods (id),
    FOREIGN KEY (channels_id) REFERENCES channels (id)
);

CREATE TABLE drinkings (
    id SERIAL PRIMARY KEY,
    date_time DATE NOT NULL,
    value REAL NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE excercise (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    excercise_type_id INTEGER NOT NULL,
    date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    location INTEGER,
    calories REAL NOT NULL,
    avg_heart_rate REAL NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (excercise_type_id) REFERENCES excercise_types(id),
    FOREIGN KEY (location) REFERENCES locations(id)
);

CREATE TABLE medical_histories (
    id SERIAL PRIMARY KEY,
    disease_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (disease_id) REFERENCES diseases(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE favorite_foods (
    user_id INTEGER NOT NULL,
    food_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, food_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (food_id) REFERENCES foods(id)
);

CREATE TABLE blog_category_mapping (
    blog_id INTEGER,
    category_id INTEGER,
    PRIMARY KEY (blog_id, category_id),
    FOREIGN KEY (blog_id) REFERENCES blogs(id),
    FOREIGN KEY (category_id) REFERENCES blog_categories(id)
);

CREATE TABLE meal_plan_foods (
    meal_plan_id INTEGER NOT NULL,
    food_id INTEGER NOT NULL,
    PRIMARY KEY (meal_plan_id, food_id),
    FOREIGN KEY (meal_plan_id) REFERENCES meal_plans(id),
    FOREIGN KEY (food_id) REFERENCES foods(id)
);

CREATE TABLE favorite_meal_plans (
    meal_plan_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (meal_plan_id, user_id),
    FOREIGN KEY (meal_plan_id) REFERENCES meal_plans(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE user_statistics (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    height REAL,
    weight REAL,
    waist_size REAL,
    userId INTEGER NOT NULL,
    FOREIGN KEY (userId) REFERENCES users(id)
);