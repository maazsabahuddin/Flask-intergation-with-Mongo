from mongoengine import *
import datetime, time
connect('Learn')


class User(Document):
    _id = ObjectIdField()
    name = StringField(required=True)
    phone_number = StringField(required=True)
    email = EmailField(required=True)
    is_active = BooleanField(default=False)
    is_admin = BooleanField(default=False)
    debit = DecimalField()
    credit = BooleanField()
    created = DateTimeField(default=datetime.datetime.now())


for user in User.objects:
    print(user.email)
