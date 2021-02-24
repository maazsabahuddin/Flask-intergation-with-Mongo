from .db import db
import datetime


class User(db.Document):
    _id = db.ObjectIdField()
    name = db.StringField(required=True)
    phone_number = db.StringField(required=True)
    email = db.EmailField(required=True)
    is_active = db.BooleanField(default=False)
    is_admin = db.BooleanField(default=False)
    debit = db.DecimalField()
    credit = db.DecimalField()
    created = db.DateTimeField(default=datetime.datetime.now())


class Post(db.Document):
    title = db.StringField(max_length=120, required=True)
    author = db.ReferenceField(User)

    meta = {'allow_inheritance': True}


class TextPost(Post):
    content = db.StringField()


class ImagePost(Post):
    image_path = db.StringField()


class LinkPost(Post):
    link_url = db.StringField()