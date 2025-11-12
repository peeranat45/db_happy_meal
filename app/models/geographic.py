from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Location(Base):
    __tablename__ = 'locations'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    latlong = Column(String)  # Using String for POINT type, consider using Geometry for PostGIS

class Region(Base):
    __tablename__ = 'regions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String)
    subRegion = Column(String)
    region = Column(String, nullable=False)