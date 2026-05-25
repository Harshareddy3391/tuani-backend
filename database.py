from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base


database_url=""

engine=create_engine(database_url)

Sessionlocal=sessionmaker(
      autocommit=False,
    autoflush=False,
   
    bind=engine
)

Base=declarative_base()