from main import db
from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.sqlite import BLOB, BOOLEAN, CHAR, DATE, DATETIME, DECIMAL, FLOAT, INTEGER, NUMERIC, SMALLINT, TEXT, TIME, TIMESTAMP, VARCHAR
from main import ma


class User(db.Model):
    user_id = db.Column(db.Integer(10))
    user_type = db.Column(db.String(255))
    name = db.Column(db.String(255))
    phone = db.Column(db.String(255), primary_key=True)
    is_otp_verified = db.Column(db.Boolean)
    address_id = db.Column(db.Integer(10))
    email = db.Column(db.String(255))
    is_email_verified = db.Column(db.Boolean)
    password = db.Column(db.String(255))
    area = db.Column(db.String(255))





    def __init__(self, userid, user_type, name, phone, is_otp_verified, address_id, email, is_email_verified, password, area):
        self.userid = userid
        self.user_type = user_type
        self.name = name
        self.phone = phone
        self.is_otp_verified = is_otp_verified
        self.address_id = address_id
        self.email = email
        self.is_email_verified = is_email_verified
        self.password = password
        self.area = area

	


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('userid', 'user_type', 'name', 'phone', 'is_otp_verified', 'address_id', 'email', 'is_email_verified', 'password', 'area')


user_schema = UserSchema()
users_schema = UserSchema(many=True)




class Order(db.Model):                                                                
    order_id = db.Column(db.Integer(10), primary_key=True)                                        
    menu_data_dump = db.Column(db.String) 
    chef_id = db.Column(db.Integer(10), db.ForeignKey('Schedule.chef_id'))                                    
    merchant_id = db.Column(db.String(255), db.ForeignKey('Schedule.merchant_id')) 
    amount = db.Column(db.Float(10))                       
    total_amount = db.Column(db.Float(10))  
    is_paid = db.Column(db.Boolean)
    is_delivered = db.Column(db.Boolean)
                                        

    def __init__(self, order_id, menu_data_dump, chef_id, merchant_id, amount, total_amount, is_paid, is_delivered):
        self.order_id = order_id
        self.menu_data_dump = menu_data_dump
        self.chef_id = chef_id
        self.merchant_id = merchant_id
        self.amount = amount
        self.total_amount = total_amount
        self.is_paid = is_paid
        self.is_delivered = is_delivered

class OrderSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('order_id', 'menu_data_dump', 'chef_id', 'merchant_id', 'amount', 'total_amount', 'is_paid', 'is_delivered')


order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)







class Menu(db.Model):                                                                
    menu_id = db.Column(db.Integer(10), primary_key=True)                                        
    chef_id = db.Column(db.Integer(10), db.ForeignKey('Schedule.chef_id'))                                    
    food_item_name = db.Column(db.String(255))                                      
    price = db.Column(db.Float(10))                                   
    day = db.Column(db.String(255))  
    is_active = db.Column(db.Boolean)                                                                     
    photo = db.Column(db.String(255))                                      


    def __init__(self, menu_id, chef_id, food_item_name, price, day, is_active, photo):
        self.menu_id = menu_id
        self.chef_id = chef_id
        self.food_item_name = food_item_name
        self.price = price
        self.day = day
        self.is_active = is_active
        self.photo = photo

class MenuSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('menu_id', 'chef_id', 'food_item_name', 'price', 'day', 'is_active', 'photo')


menu_schema = MenuSchema()
menus_schema = MenuSchema(many=True)





class Schedule(db.Model):         
    schedule_id = db.Column(db.Integer(10), primary_key=True)                                                                                       
    menu_data_dump = db.Column(db.NVARCHAR) 
    chef_id = db.Column(db.String(255))                                    
    merchant_id = db.Column(db.Integer(10))                                      
    amount = db.Column(db.Float(10))                       
    total_amount = db.Column(db.Float(10))                       
    date  = db.Column(db.DateTime)      

    def __init__(self, schedule_id, menu_data_dump, chef_id, merchant_id, amount, total_amount, date):
        self.schedule_id = schedule_id
        self.menu_data_dump = menu_data_dump
        self.chef_id = chef_id
        self.merchant_id = merchant_id
        self.amount = amount
        self.total_amount = total_amount
        self.date = date

      


class ScheduleSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('schedule_id', 'menu_data_dump', 'chef_id', 'merchant_id', 'amount', 'total_amount', 'date')


schedule_schema = ScheduleSchema()
schedules_schema = ScheduleSchema(many=True)







class Address(db.Model):                                                                
    address_id = db.Column(db.Integer(10), primary_key=True)                                        
    user_type = db.Column(db.String(255))                                    
    user_id = db.Column(db.Integer(10), db.ForeignKey('User.user_id'))
    latitude = db.Column(db.Float(255))                                    
    longitude = db.Column(db.Float(255))    
    address_line_one = db.Column(db.String(255))    
    address_line_two = db.Column(db.String(255))    
    pincode = db.Column(db.String(255))    
    city = db.Column(db.String(255))    
    landmark = db.Column(db.String(255))    

                              

      

    def __init__(self, address_id, user_type, hotel_id, latitude, longitude, address_line_one, address_line_two, pincode, city, landmark):
        self.address_id = address_id
        self.user_type = user_type
        self.hotel_id = hotel_id
        self.latitude = latitude
        self.longitude = longitude
        self.address_line_one = address_line_one
        self.address_line_two = address_line_two
        self.pincode = pincode
        self.city = city
        self.landmark = landmark


class AddressSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('address_id', 'user_type', 'hotel_id', 'latitude', 'longitude', 'address_line_one', 'address_line_two', 'pincode', 'city', 'landmark')


address_schema = AddressSchema()
addresss_schema = AddressSchema(many=True)