from sqlmodel import Field, SQLModel 

class Locations(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    type: str
    lat: float
    long: float