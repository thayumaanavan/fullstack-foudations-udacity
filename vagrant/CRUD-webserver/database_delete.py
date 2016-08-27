from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base,Restaurant,MenuItem

engine=create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind=engine
DBSession=sessionmaker(bind=engine)
session=DBSession()

#spinach=session.query(MenuItem).filter_by(name='Spinach Ice Cream').one()
#print spinach.restaurant.name
#session.delete(spinach)
#spinach=session.query(MenuItem).filter_by(name='Spinach Ice Cream').one()
session.query(Restaurant).delete()
session.query(MenuItem).delete()
session.commit()
#for restaurant in restaurantList:
 #   session.delete(restaurant)

restaurantList=session.query(Restaurant).all()
for restaurant in restaurantList:
    print restaurant.name
