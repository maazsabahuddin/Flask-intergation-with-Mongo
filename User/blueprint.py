from flask import Blueprint
from User.views import hello_world, login, user_data, get_users, add_user

my_view = Blueprint('my_view', __name__)
my_view.add_url_rule('/home', view_func=hello_world, methods=['GET', 'POST'])
my_view.add_url_rule('/', view_func=hello_world, methods=['GET', 'POST'])
my_view.add_url_rule('/db', view_func=user_data, methods=['GET', 'POST'])
my_view.add_url_rule("/login/", view_func=login, methods=['GET', 'POST'])
my_view.add_url_rule("/user/", view_func=get_users, methods=['GET', 'POST'])
my_view.add_url_rule("/add/user/", view_func=add_user, methods=['POST'])
