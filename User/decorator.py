from functools import wraps

from flask.views import View
from flask import jsonify, request
import jwt
from flask.views import MethodView
from User.exception import TokenException, MissingBody, UserException
from User.models import User


def token_required(f):

    @wraps(f)
    def decorator(*args):

        try:
            request_arguments = request.args
            payload = request.get_json()
            if not payload:
                raise MissingBody(status_code=400, message="body is missing")

            token = payload.get('token')
            if not token:
                raise TokenException(status_code=401, message="Token missing")

            from setting.app import app
            obj = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
            if not obj:
                raise TokenException(status_code=401, message="Invalid token")

            data = obj.get('data')
            email = data.get('email')
            user = User.objects.filter(email=email).first()
            if not user:
                raise TokenException(status_code=401, message="Invalid token")

            return f(*args, payload, user)

        except (TokenException, MissingBody) as e:
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


class ValidateJWT(MethodView):
    # methods = ['GET']

    @token_required
    def get(self, payload, user=None):

        try:
            if not user:
                raise UserException(status_code=404, message='User does not exist.')

            return jsonify({
                'email': user.email,
                'message': 'Validated'
            })

        except UserException as e:
            return jsonify({
                'email': user.email,
                'status': e.status_code,
                'message': e.message
            })

        except Exception as e:
            return jsonify({
                'status': 400,
                'internal_message': str(e),
                'message': 'Exception occurred'
            })

    def post(self):
        return jsonify({
            'status': 405,
            'message': 'Method Not Allowed'
        })
