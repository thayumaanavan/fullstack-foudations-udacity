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
    #for item in items:
     #   print item.name
    return items

#list_all_restaurant()
    
#Used for webserver CRUD
def create_restaurant(restaurant_name):
    restaurant=Restaurant(name=restaurant_name)
    session.add(restaurant)
    session.commit()

def get_restaurant(id):
    restaurant=session.query(Restaurant).filter_by(id=id).one()
    return restaurant

def update_restaurant(id,name):
    restaurant=get_restaurant(id)
    restaurant.name=name
    session.add(restaurant)
    session.commit()

def delete_restaurant(id):
    restaurant=get_restaurant(id)
    session.delete(restaurant)
    session.commit()

def get_menu_item_by_restaurant(restaurant_id):
    item=session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return item;

def get_menu_item(menu_id):
    item=session.query(MenuItem).filter_by(id=menu_id).one()
    return item

def update_Menu(menu_id,name):
    menu=get_menu_item(menu_id)
    if name:
        menu.name=name
    session.add(menu)
    session.commit()

def delete_menu(menu_id):
    item=get_menu_item(menu_id)
    session.delete(item)
    session.commit()