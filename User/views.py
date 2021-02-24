import ast
import json
import jwt
from flask.views import View
import flask
from flask import jsonify, request, Response
from flask_api import status
from markupsafe import escape

from .exception import InvalidArguments, NotANumber
from .models import User
from .dto import UserDTO
from functools import wraps
from .seriazable import dumper


def calc_decorator(f):

    def decorator(*args):
        try:
            request_arguments = request.args
            if not request_arguments:
                raise InvalidArguments(status_code=400, message="No arguments found")

            op = request_arguments.get('op')
            if not op:
                raise InvalidArguments(status_code=400, message="op argument missing.")

            if op == '+':
                op = '-'

            elif op == '-':
                op = '+'

            return f(op=op)

        except InvalidArguments as e:
            return jsonify({
                'status': e.status_code,
                'message': e.message
            })

        except Exception as e:
            return jsonify({
                'status': 400,
                'message': "Something went wrong.",
                'internal_message': str(e)
            })

    return decorator


def isNumber(**kwargs):
    op1 = kwargs.get('op1')
    op2 = kwargs.get('op2')

    try:
        int(op1)
        int(op2)
        return True
    except:
        return False


def calculation(**kwargs):
    op1 = kwargs.get('op1')
    op2 = kwargs.get('op2')
    op = kwargs.get('op')

    if op == '+':
        return int(op1)+int(op2)
    elif op == '-':
        return int(op1)-int(op2)
    else:
        return None


@calc_decorator
def calc(**kwargs):
    try:
        op_decorator = kwargs.get('op')
        request_arguments = request.args
        if not request_arguments:
            raise InvalidArguments(status_code=400, message="No arguments found")

        op1 = request_arguments.get('op1')
        op2 = request_arguments.get('op2')
        op = request_arguments.get('op')

        if not (op1 and op2 and op):
            raise InvalidArguments(status_code=400, message="Some of the arguments are missing.")

        if not isNumber(op1=op1, op2=op2):
            raise NotANumber(status_code=400, message="op1 and op2 are not numeric value.")

        result = None
        if op_decorator:
            result = calculation(op1=op1, op2=op2, op=op_decorator)
        else:
            result = calculation(op1=op1, op2=op2, op=op)

        if not result:
            raise NotANumber(status_code=400, message="op is not a sign.")

        return jsonify({
            'status': 200,
            'result': result
        })

    except (InvalidArguments, NotANumber) as e:
        return jsonify({
            'status': e.status_code,
            'message': e.message
        })

    except Exception as e:
        return jsonify({
            'status': 400,
            'message': "Something went wrong.",
            'internal_message': str(e)
        })


def hello_world():
    return 'Hello, World!'


def api(username):
    return 'Admin: {}'.format(escape(username))


class Login(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        try:
            data = request.get_json()
            # hashed_password = generate_password_hash(data['password'], method='sha256')
            # user = Users(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password, admin=False).save()

            user = User.objects(email="maazsabahuddin@gmail.com").first()
            if not user:
                return jsonify({
                    'message': 'Invalid email',
                })

            from setting.app import app
            # You can also add the time validity.
            token = jwt.encode({'data': data}, app.config['SECRET_KEY'], algorithm='HS256')

            return jsonify({
                'status': status.HTTP_200_OK,
                'token': token.decode('UTF-8')
            })

        except Exception as e:
            return jsonify({
                'message': str(e),
            })


def get_users():
    try:
        request_arguments = request.args
        if not request_arguments:
            raise InvalidArguments(status_code=400, message="No arguments found")

        email = request_arguments.get('email')
        if not email:
            raise InvalidArguments(status_code=400, message="Email not found.")

        user = User.objects(email=email).first()
        if not user:
            return jsonify({
                'status': 200,
                'data': [],
                'message': 'No data'
            })
        user_data_obj = UserDTO(name=user.name, email=user.email, phone_number=user.phone_number,
                                is_active=user.is_active,
                                is_admin=user.is_admin, debit=user.debit, credit=user.credit, created=user.created)
        data = user_data_obj.returndtodata()
        # data = json.dumps(user_data_obj, default=dumper)

        # return Response(data1, mimetype="application/json", status=200)
        return jsonify({
            'status': 200,
            'data': data,
            'message': 'successful'
        })

    except InvalidArguments as e:
        return jsonify({
            'status': e.status_code,
            'message': e.message
        })

    except Exception as e:
        return jsonify({
            'status': 400,
            'message': "Something went wrong.",
            'internal_message': str(e)
        })


def add_user():
    try:
        body = request.get_json()
        token = flask.request.headers.get('Authorization')

        if not body:
            return jsonify({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Missing body',
            })

        user = User(**body).save()

        return jsonify({
            'status': status.HTTP_200_OK,
            'message': 'User Added',
        })

    except Exception as e:
        return jsonify({
            'status': 400,
            'message': "Something went wrong.",
            'internal_message': str(e)
        })
