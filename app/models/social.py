from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

Base = declarative_base()

class SocialPlatform(Base):
    __tablename__ = 'social_platforms'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)

class UserSocialAccount(Base):
    __tablename__ = 'user_social_accounts'
    
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    platform_id = Column(Integer, ForeignKey('social_platforms.id'), primary_key=True)
    connected_at = Column(DateTime, server_default=func.now())
    
    user = relationship("User", back_populates="social_accounts")
    platform = relationship("SocialPlatform")