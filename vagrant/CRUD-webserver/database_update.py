from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base,Restaurant,MenuItem

engine=create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind=engine
DBSession=sessionmaker(bind=engine)
session=DBSession()


#update
veggieBurgers=session.query(MenuItem).filter_by(name='Veggie Burger')

for veggieBurger in veggieBurgers:
    if(veggieBurger.price !='$.2.99'):
        veggieBurger.price='$2.99'
        session.add(veggieBurger)
        session.commit()

for veggieBurger in veggieBurgers:
    print veggieBurger.id
    print veggieBurger.price
    print "\n"


