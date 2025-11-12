from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Disease(Base):
    __tablename__ = 'diseases'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    disease_name = Column(String, nullable=False)
    description = Column(String, nullable=False)

class MedicalHistory(Base):
    __tablename__ = 'medical_histories'
    
    id = Column(Integer, primary_key=True)
    disease_id = Column(Integer, ForeignKey('diseases.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    
    disease = relationship("Disease")
    user = relationship("User", back_populates="medical_histories")