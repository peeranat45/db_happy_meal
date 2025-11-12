CREATE TABLE user_statistics (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    height REAL,
    weight REAL,
    waist_size REAL,
    userId INTEGER NOT NULL,

    FOREIGN KEY (userId) REFERENCES users(id)
);