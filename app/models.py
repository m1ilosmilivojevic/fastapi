from sqlalchemy import TIMESTAMP, Column, DateTime, ForeignKey, Integer, String, Boolean, func
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import Null
from .database import Base

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True, nullable=False)
    content = Column(String(255), index=True, nullable=False)
    published = Column(Boolean, default=True, nullable=False)  
    created_at = Column(DateTime, default=func.now())
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    
    owner = relationship("User")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now())
    phone_number = Column(String(255))

class Vote(Base):
    __tablename__= "votes"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key="True")
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key="True")
