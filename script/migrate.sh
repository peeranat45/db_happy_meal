
# Generating new migration
alembic revision --autogenerate -m "auto migration"
# Apply Migration
alembic upgrade head

# Generate SQL
alembic upgrade head --sql > upgreade.sql