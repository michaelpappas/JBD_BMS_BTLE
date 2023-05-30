from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Battery, db_url


db = create_engine(db_url)

Session = sessionmaker(db)
session = Session()

def add_to_db():
    """ Add sample data to the battery db table."""
    new_battery = Battery(volts = 1234.5,
                              amps = 1234.5,
                              capactity = 1234.5,
                              remain = 1234.5,
                              percent = 1234.5,
                              temp1 = 1234.5,
                              temp2 = 1234.5,
                              cell1 = 1234.5,
                              cell2 = 1234.5,
                              cell3 = 1234.5,
                              cell4 = 1234.5,
                              )
    session.add(new_battery)
    session.commit()

add_to_db()
