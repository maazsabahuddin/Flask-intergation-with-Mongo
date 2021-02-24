from flask import Blueprint

from User.decorator import ValidateJWT
from User.views import hello_world, Login, get_users, add_user, calc

my_view = Blueprint('my_view', __name__)
my_view.add_url_rule('/home', view_func=hello_world, methods=['GET', 'POST'])
my_view.add_url_rule('/', view_func=hello_world, methods=['GET', 'POST'])
my_view.add_url_rule("/login/", view_func=Login.as_view('login_view'), methods=['GET', 'POST'])
my_view.add_url_rule("/users/", view_func=get_users, methods=['GET', 'POST'])
my_view.add_url_rule("/add/user/", view_func=add_user, methods=['POST'])
my_view.add_url_rule("/validate/token/", view_func=ValidateJWT.as_view('validate_token'))
my_view.add_url_rule("/calc/", view_func=calc, methods=['GET'])
