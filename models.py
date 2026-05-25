from sqlalchemy import Column,Integer,String,Text


from database import Base


class Contact(Base):

    __tablename__="contacts"

    id=Column(Integer, index=True,primary_key=True)
    full_name=Column(String)
    email=Column(String)
    phone=Column(String)
    message=Column(Text)
