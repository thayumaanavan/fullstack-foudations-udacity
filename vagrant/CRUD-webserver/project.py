from flask import Flask,render_template,request,redirect,url_for
import database_CRUD
app=Flask(__name__)

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant=database_CRUD.get_restaurant(restaurant_id)
    items=database_CRUD.get_menu_item_by_restaurant(restaurant_id)
    return render_template('menu.html',restaurant=restaurant,items=items)
    

# Task 1: Create route for newMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/new/')
def newMenuItem(restaurant_id):
    return "page to create a new menu item. Task 1 complete!"

# Task 2: Create route for editMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/',methods=['GET','POST'])
def editMenuItem(restaurant_id, menu_id):
    if request.method == 'POST':
        name=request.form['name']
        editedItem=database_CRUD.update_Menu(menu_id,name)
        return redirect(url_for('restaurantMenu',restaurant_id=restaurant_id))
    else:
        editedItem=database_CRUD.get_menu_item(menu_id)
        return render_template('editMenuItem.html',restaurant_id=restaurant_id,menu_id=menu_id,item=editedItem)


# Task 3: Create a route for deleteMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/',
            methods=['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
    if request.method == 'POST':
        database_CRUD.delete_menu(menu_id)
        return redirect(url_for('restaurantMenu',restaurant_id=restaurant_id))
    else:
        menu=database_CRUD.get_menu_item(menu_id)
        return render_template('deleteMenuItem.html',restaurant_id=restaurant_id,menu_id=menu_id,item=menu)


if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
