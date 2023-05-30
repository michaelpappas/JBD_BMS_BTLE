from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Battery, db_url


db = create_engine(db_url)

Session = sessionmaker(db)
session = Session()

def add_to_db():
    """ Add sample data to the battery db table."""
    new_battery = Battery(volts = 13.24,
                              amps = -1.08,
                              capacity = 180.0,
                              remain = 170.51,
                              percent = 95,
                              temp1 = 16.8,
                              temp2 = 16.7,
                              cell1 = 3320,
                              cell2 = 3321,
                              cell3 = 3317,
                              cell4 = 3284,
                              )
    session.add(new_battery)
    session.commit()

add_to_db()
