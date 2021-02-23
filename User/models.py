from .db import db


class User(db.Document):
    company_name = db.StringField(required=True)
    phone_number = db.StringField(required=True)
    email = db.StringField(required=True)
    is_active = db.BooleanField(default=False)
    is_admin = db.BooleanField(default=False)


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