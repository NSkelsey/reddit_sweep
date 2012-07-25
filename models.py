from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, String, ForeignKey, DATETIME
from sqlalchemy.orm import sessionmaker, relationship, backref

engine = create_engine("sqlite:///sweep.db", echo=False)

Base = declarative_base()

class Comment(Base):
    __tablename__ = "comment_table"
    id = Column(Integer, primary_key=True)
    upvotes = Column(Integer)
    text = Column(String)
    parent_id = Column(Integer, ForeignKey('comment_table.id'))
    children = relationship("Comment", 
            backref=backref('parent', remote_side=[id]),
                )
    user_name = Column(String, ForeignKey("user_table.name"))
    user = relationship("User", backref=backref("comments"))
    post_name = Column(String, ForeignKey("post_table.name"))
    post = relationship("Post", backref=backref("comments"))
    date_of_last_sweep = Column(DATETIME)

class User(Base):
    __tablename__  = "user_table"
    name = Column(String, primary_key=True)

class Post(Base):
    __tablename__ = "post_table"
    name = Column(String, primary_key=True)
    url = Column(String)
    upvotes = Column(Integer)



if __name__ == "__main__":
    Base.metadata.create_all(engine)
    
    
Session = sessionmaker(bind=engine)
session = Session()

