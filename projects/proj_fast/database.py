from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#install conector:  pip install psycopg2-binary
engine=create_engine("postgresql://postgres:postgres@localhost/item_db",
                     echo=True)

Base =  declarative_base()

SessionLocal=sessionmaker(bind=engine)


