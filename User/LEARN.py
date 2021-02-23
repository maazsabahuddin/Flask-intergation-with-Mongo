from mongoengine import *
import datetime
connect('Learn')


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    company_name = StringField(required=True)
    phone_number = StringField(required=True)
    is_active = BooleanField(default=False)
    is_admin = BooleanField(default=False)
    password = StringField()
    created_date = BooleanField(default=datetime.datetime.now())
    last_login = BooleanField(default=datetime.datetime.now())
    address = StringField()


for user in User.objects:
    print(user.email)
