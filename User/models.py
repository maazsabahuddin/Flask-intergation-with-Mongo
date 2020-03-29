from .db import db


class User(db.Document):
    name = db.StringField(required=True, unique=True)
    department = db.StringField(required=True)
    role = db.ListField(db.StringField(), required=True)
