import datetime
from sqlalchemy import create_engine, Column, DateTime, Float, Numeric
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()
# Configure the PostgreSQL connection
db_user = 'admin'
db_password = os.environ['db_password']
# db_password = 'postgres'
db_host = 'localhost'
db_port = '5432'
db_name = 'van_data'

db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
# Create a database connection
engine = create_engine(db_url)

# Create a base class for declarative table definitions
Base = declarative_base()

# Define the Battery class representing the table
class Battery(Base):
    __tablename__ = 'battery'

    timestamp = Column(
                        DateTime,
                        primary_key=True,
                        default=datetime.datetime.utcnow)
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

# Create the table in the database
Base.metadata.create_all(engine)






