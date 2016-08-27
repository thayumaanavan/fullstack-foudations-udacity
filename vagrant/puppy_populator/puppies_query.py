from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from puppies import Base, Shelter, Puppy
#from flask.ext.sqlalchemy import SQLAlchemy
import datetime


engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

def query_one():
    puppies=session.query(Puppy).order_by(Puppy.name.asc()).all()
    for puppy in puppies:
        print puppy.name

#query_one()

def query_two():
    today = datetime.date.today()
    if passesLeapDay(today):
        sixMonthsAgo = today - datetime.timedelta(days = 183)
    else:
        sixMonthsAgo = today - datetime.timedelta(days = 182)
    puppies = session.query(Puppy.name, Puppy.dateOfBirth)\
        .filter(Puppy.dateOfBirth >= sixMonthsAgo)\
        .order_by(Puppy.dateOfBirth.desc())
    for puppy in puppies:
        print puppy.name

# Helper Methods
def passesLeapDay(today):
    """
    Returns true if most recent February 29th occured after or exactly 183 days ago (366 / 2)
    """
    thisYear = today.timetuple()[0]
    if isLeapYear(thisYear):
        sixMonthsAgo = today - datetime.timedelta(days = 183)
        leapDay = datetime.date(thisYear, 2, 29)
        return leapDay >= sixMonthsAgo
    else:
        return False
        
def isLeapYear(thisYear):
    """
    Returns true iff the current year is a leap year.
    Implemented according to logic at https://en.wikipedia.org/wiki/Leap_year#Algorithm
    """
    if thisYear % 4 != 0:
        return False
    elif thisYear % 100 != 0:
        return True
    elif thisYear % 400 != 0:
        return False
    else:
        return True


def query_three():
    puppies=session.query(Puppy).order_by(Puppy.weight.asc()).all()
    for puppy in puppies:
        print puppy.name

def query_four():
    items=session.query(Shelter,func.count(Puppy.id)).join(Puppy)\
            .group_by(Shelter.id).all()
    for item in items:
        print item[0].id,item[0].name,item[1]




#query_one()
#query_two()
#query_three()
query_four()