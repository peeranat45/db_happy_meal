--- meals

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

--- food_meals

CREATE TABLE food_meals (
    meal_id INTEGER NOT NULL,
    food_id INTEGER NOT NULL,
    channels_id INTEGER,
    price REAL,

    FOREIGN KEY (meal_id) REFERENCES meals (id),
    FOREIGN KEY (food_id) REFERENCES foods (id),
    FOREIGN KEY (channels_id) REFERENCES channels (id)
);

--- drinkings

CREATE TABLE drinkings (
    id INTEGER PRIMARY KEY,
    date_time DATE NOT NULL,
    value REAL NOT NULL,
    user_id INTEGER NOT NULL,

    FOREIGN KEY (user_id) REFERENCES users(id)
);

--- exercises

CREATE TABLE excercise (
    id INTEGER PRIMARY KEY,
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

--- medical_history

CREATE TABLE medical_histories (
	id INTEGER PRIMARY KEY,
	disease_id INTEGER NOT NULL,
	user_id INTEGER NOT NULL,
	start_date DATE,
	end_date DATE,

	FOREIGN KEY (disease_id) REFERENCES diseases(id),
	FOREIGN KEY (user_id) REFERENCES users(id)
);

--- favorite food
CREATE TABLE favorite_foods (
    user_id INTEGER NOT NULL,
    food_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (user_id, food_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (food_id) REFERENCES foods(id)
);

--- blog
CREATE TABLE blogs (
	id INTEGER PRIMARY KEY,
	blog_name TEXT NOT NULL,
	content TEXT NOT NULL ,
	published_at DATE,
	views INTEGER,
    likes INTEGER
);

CREATE TABLE blog_category_mapping (
    blog_id INTEGER,
    category_id INTEGER,
    
    PRIMARY KEY (blog_id, category_id),
    FOREIGN KEY (blog_id) REFERENCES blogs(id),
    FOREIGN KEY (category_id) REFERENCES blog_categories(id)
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
