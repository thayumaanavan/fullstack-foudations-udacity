from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base,Restaurant,MenuItem

engine=create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind=engine
DBSession=sessionmaker(bind=engine)
session=DBSession()

def list_all_restaurant():
    #read
    items=session.query(Restaurant).all()
    for item in items:
        print item.name
    return items

#list_all_restaurant()
    
#Used for webserver CRUD
def create_restaurant(restaurant_name):
    restaurant=Restaurant(name=restaurant_name)
    session.add(restaurant)
    session.commit()

