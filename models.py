from sqlalchemy import create_engine, Column, Integer, String, DateTime, Numeric, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Configure the PostgreSQL connection
db_user = ''
db_password = os.environ['db_password']
db_host = 'localhost'
db_port = '5432'
db_name = 'van_data'

# Create the PostgreSQL connection URL
db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

# Create a database engine and session
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

# Create a base class for declarative models
Base = declarative_base()

# Define your table model classes
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

# Create the tables
Base.metadata.create_all(engine)


class Battery(Base):
    """ Battery Data """

    __tablename__= 'battery'

    timestamp = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    volts = Column(
        Numeric,
        nullable=False,
        unique=False
    )
    amps = Column(
        Numeric,
        nullable=False,
        unique=False
    )
    capacity = Column(
        Numeric,
        nullable=False,
        unique=False
    )
    remain = Column(
        Numeric,
        nullable=False,
        unique=False
    )
    percent = Column(
        Numeric,
        nullable=False,
        unique=False
    )
    temp1 = Column(
        Numeric,
        nullable=False,
        unique=False
    )
    temp2 = Column(
        Numeric,
        nullable=False,
        unique=False
    )
    cell1 = Column(
        Float,
        nullable=False,
        unique=False
    )
    cell2 = Column(
        Float,
        nullable=False,
        unique=False
    )
    cell3 = Column(
        Float,
        nullable=False,
        unique=False
    )
    cell4 = Column(
        Float,
        nullable=False,
        unique=False
    )







