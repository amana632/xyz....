from flask import request, jsonify
from main import app
from flask_marshmallow import Marshmallow
from main import db
from main.model import User, UserSchema, user_schema, users_schema, Order, OrderSchema, order_schema, orders_schema, Menu, MenuSchema, menu_schema, menus_schema, Schedule, ScheduleSchema, schedule_schema, schedules_schema, Address, AddressSchema, address_schema, addresss_schema

@app.route("/isRegisteredUser/<phone>", methods=["GET"])
def isRegisteredUser(phone):
    data = User.query.get(phone)
    if (data.phone != phone) :
        return False
    else :
        return True

@app.route("/isValidUser", methods=["GET"])
def isValidUser():
    phone = request.form['phone']
    password = request.form['password']
    user_type = request.form['user_type']



    data = User.query.get(phone)

    if(data.password == password & data.user_type == user_type) :
        return True
    else :
        return False



@app.route("/doRegistration", methods=["POST"])
def doRegistration():

    user_id = request.form['user_id']
    user_type = request.form['user_type']
    name = request.form['name']
    phone = request.form['phone']
    is_otp_verified = request.form['is_otp_verified']
    address_id = request.form['address_id']
    email = request.form['email']
    is_email_verified = request.form['is_email_verified']
    password = request.form['password']
    area = request.form['area']

    new_user = User(user_id, user_type, name, phone, is_otp_verified, address_id, email, is_email_verified, password, area)

    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user)



@app.route("/getRegistration/<phone>", methods=["GET"])
def reg_detail(phone):
    user = User.query.get(phone)
    return user_schema.jsonify(user)



# endpoint to update user
@app.route("/updateRegistration/<phone>", methods=["PUT"])
def reg_update(phone):
    user = User.query.get(phone)

    user_id = request.form['user_id']
    user_type = request.form['user_type']
    name = request.form['name']
    phone = request.form['phone']
    is_otp_verified = request.form['is_otp_verified']
    address_id = request.form['address_id']
    email = request.form['email']
    is_email_verified = request.form['is_email_verified']
    password = request.form['password']
    area = request.form['area']


    user.user_id = user_id
    user.user_type = user_type
    user.name = name
    user.phone = phone
    user.is_otp_verified = is_otp_verified
    user.address_id = address_id
    user.email = email
    user.is_email_verified = is_email_verified
    user.password = password
    user.area = area
 

    db.session.commit()
    return user_schema.jsonify(user)



# endpoint to delete user
@app.route("/deleteRegistration/<phone>", methods=["DELETE"])
def user_delete(phone):
    user = User.query.get(phone)
    db.session.delete(user)
    db.session.commit()

    return order_schema.jsonify(user)




@app.route("/postSchedule", methods=["POST"])
def addSchedule():

    schedule_id = request.form['schedule_id']                                                                                    
    menu_data_dump = request.form['menu_data_dump']
    chef_id = request.form['chef_id']                          
    merchant_id = request.form['merchant_id']                                    
    amount = request.form['amount_id']             
    total_amount = request.form['total_amount']                     
    date  = request.form['date']


    new_schedule = Schedule(schedule_id, menu_data_dump, chef_id, merchant_id, amount, total_amount, date)

    db.session.add(new_schedule)
    db.session.commit()
    return jsonify(new_schedule)


@app.route("/getSchedule/<phone>", methods=["GET"])
def schedule_detail(phone):
    schedule = Schedule.query.get(phone)
    return schedule_schema.jsonify(schedule)



# endpoint to update schedule
@app.route("/updateSchedule/<phone>", methods=["PUT"])
def schedule_update(phone):
    schedule = Schedule.query.get(phone)

    schedule_id = request.form['schedule_id']                                                                                    
    menu_data_dump = request.form['menu_data_dump']
    chef_id = request.form['chef_id']                          
    merchant_id = request.form['merchant_id']                                    
    amount = request.form['amount_id']             
    total_amount = request.form['total_amount']                     
    date  = request.form['date']


    schedule.schedule_id = schedule_id
    schedule.menu_data_dump = menu_data_dump
    schedule.chef_id = chef_id
    schedule.merchant_id = merchant_id
    schedule.amount = amount
    schedule.total_amount = total_amount
    schedule.date = date
 

    db.session.commit()
    return schedule_schema.jsonify(schedule)

@app.route("/deleteSchedule/<phone>", methods=["DELETE"])
def schedule_delete(phone):
    schedule = Schedule.query.get(phone)
    db.session.delete(schedule)
    db.session.commit()

    return schedule_schema.jsonify(schedule)



@app.route("/postOrder", methods=["POST"])
def addOrder():

    order_id = request.form['order_id']                                             
    menu_data_dump = request.form['menu_data_dump']            
    chef_id = request.form['chef_id']                                           
    merchant_id = request.form['merchant_id']            
    amount = request.form['amount']            
    total_amount = request.form['total_amount']            
    is_paid = request.form['is_paid']            
    is_delivered = request.form['is_delievered']            
    
    
    
    new_order = Order(order_id, menu_data_dump, chef_id, merchant_id, amount, total_amount, is_paid, is_delivered)

    db.session.add(new_order)
    db.session.commit()
    return jsonify(new_order)



@app.route("/getUserOrder/<ids>", methods=["GET"])
def orders_detail(ids):
    orders = Order.query.filter_by(order_id=ids).first()
    return order_schema.jsonify(orders)



# endpoint to show all users
@app.route("/getAllOrder", methods=["GET"])
def get_order():
    all_orders = Order.query.all()
    result = orders_schema.dump(all_orders)
    return jsonify(result.data)



@app.route("/postMenu", methods=["POST"])
def addMenu():        
    
    menu_id = request.form['menu_id']                              
    chef_id = request.form['chef_id']                                               
    food_item_name = request.form['food_item_name']                                             
    price = request.form['price']                                         
    day = request.form['day']            
    is_active = request.form['is_active']                                                                         
    photo = request.form['photo']            
    
    new_menu = Menu( menu_id, chef_id, food_item_name, price, day, is_active, photo)

    db.session.add(new_menu)
    db.session.commit()
    return jsonify(new_menu)





@app.route("/getMenu/<ids>", methods=["GET"])
def menus_detail(ids):
    menus = Menu.query.filter_by(menu_id=ids).first()
    return menu_schema.jsonify(menus)


@app.route("/updateMenu/<phone>", methods=["PUT"])
def menu_update(phone):
    menu = Menu.query.get(phone)

    menu_id = request.form['menu_id']                              
    chef_id = request.form['chef_id']                                               
    food_item_name = request.form['food_item_name']                                             
    price = request.form['price']                                         
    day = request.form['day']            
    is_active = request.form['is_active']                                                                         
    photo = request.form['photo']     


    menu.menu_id = menu_id
    menu.chef_id = chef_id
    menu.food_item_name = food_item_name
    menu.price = price
    menu.day = day
    menu.is_active = is_active
    menu.photo = photo
 

    db.session.commit()
    return menu_schema.jsonify(menu)


