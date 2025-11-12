-- User

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

-- geographics

---- location

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    latlong POINT
);
---- regions

CREATE TABLE regions (
    id SERIAL PRIMARY KEY,
    country TEXT,
    subRegion TEXT,
    region TEXT NOT NULL
);

-- Food

---- meal_types

CREATE TABLE meal_types (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

---- foods

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

---- ingredients

CREATE TABLE ingredients (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE food_ingredients (
    food_id INTEGER NOT NULL,
    ingredients_id INTEGER,
    amount REAL NOT NULL,
    unit TEXT NOT NULL,

    FOREIGN KEY (food_id) REFERENCES foods (id),
    FOREIGN KEY (ingredients_id) REFERENCES ingredients (id)
);

---- channels

CREATE TABLE channels (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);


-- Acivities

---- excercise_types

CREATE TABLE excercise_types (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL 
);


-- Health

---- diseases

CREATE TABLE diseases (
	id SERIAL PRIMARY KEY,
	disease_name TEXT NOT NULL,
	description TEXT NOT NULL
);

-- Social Media

---- social_platforms

CREATE TABLE social_platforms (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

---- user_social_accounts 

CREATE TABLE user_social_accounts (
	user_id INTEGER NOT NULL,
	platform_id  INTEGER NOT NULL,
    connected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
	FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (platform_id) REFERENCES social_platforms(id)
);

-- Blog

CREATE TABLE blog_categories (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

-- Meal Plan
CREATE TABLE meal_plan_types (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);