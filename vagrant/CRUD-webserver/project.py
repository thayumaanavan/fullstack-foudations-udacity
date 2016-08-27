from flask import Flask,render_template,request,redirect,url_for,flash,jsonify
import database_CRUD
app=Flask(__name__)

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant=database_CRUD.get_restaurant(restaurant_id)
    items=database_CRUD.get_menu_item_by_restaurant(restaurant_id)
    return render_template('menu.html',restaurant=restaurant,items=items)
    
#API Endpoint json (GET)
@app.route('/restaurants/<int:restaurant_id>/menu/JSON/')
def restaurantMenuJSON(restaurant_id):
    restaurant=database_CRUD.get_restaurant(restaurant_id)
    items=database_CRUD.get_menu_item_by_restaurant(restaurant_id)
    return jsonify(MenuItems=[i.serialize for i in items])

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON/')
def menuItem(restaurant_id,menu_id):
    return jsonify(MenuItem=database_CRUD.get_menu_item(menu_id).serialize)
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
        flash("Item Edited successfully")
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
        flash("Item Deleted successfully")
        return redirect(url_for('restaurantMenu',restaurant_id=restaurant_id))
    else:
        menu=database_CRUD.get_menu_item(menu_id)
        return render_template('deleteMenuItem.html',restaurant_id=restaurant_id,menu_id=menu_id,item=menu)


if __name__=='__main__':
    app.secret_key='super_secret_key'
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
