from sqlalchemy import Boolean, Column , Integer , String , TIMESTAMP , text , ForeignKey
from sqlalchemy.orm import Relationship
from sqlalchemy.sql.expression import null
from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id =  Column(Integer , primary_key = True , nullable = False)
    title = Column(String , nullable = False)
    content = Column(String , nullable = False)
    published = Column(Boolean , nullable = False , server_default = 'True')
    created_at = Column(TIMESTAMP(timezone = True) , nullable = False , server_default = text('now()'))
    owner_id = Column(Integer , ForeignKey("users.id" , ondelete = "CASCADE") , nullable = False)

    owner = Relationship("User")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer , primary_key = True , nullable = False)
    email = Column(String , nullable = False , unique = True)
    password = Column(String , nullable = False)
    created_at = Column(TIMESTAMP(timezone = True) , nullable = False , server_default = text('now()'))

class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer , ForeignKey("users.id" , ondelete = "CASCADE") , primary_key = True)
    post_id = Column(Integer , ForeignKey("posts.id" , ondelete = "CASCADE") , primary_key = True)