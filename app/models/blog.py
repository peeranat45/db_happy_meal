from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

blog_category_mapping = Table('blog_category_mapping', Base.metadata,
    Column('blog_id', Integer, ForeignKey('blogs.id'), primary_key=True),
    Column('category_id', Integer, ForeignKey('blog_categories.id'), primary_key=True)
)

class BlogCategory(Base):
    __tablename__ = 'blog_categories'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    
    blogs = relationship("Blog", secondary=blog_category_mapping, back_populates="categories")

class Blog(Base):
    __tablename__ = 'blogs'
    
    id = Column(Integer, primary_key=True)
    blog_name = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    published_at = Column(Date)
    views = Column(Integer)
    likes = Column(Integer)
    
    categories = relationship("BlogCategory", secondary=blog_category_mapping, back_populates="blogs")