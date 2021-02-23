import ast
import json

import flask
from flask import jsonify, request, Response
from flask_api import status
from markupsafe import escape
from .models import User
from .dto import UserDTO
from .seriazable import dumper


def hello_world():
    return 'Hello, World!'


def api(username):
    return 'Admin: {}'.format(escape(username))


def login():
    data = {
        'status': status.HTTP_200_OK,
        'token': 'AasdJdAH2h91dhajsdkaDAHDsdD_1',
        'message': 'Login successfully.',
    }
    return jsonify(data)


def get_users():
    user = User.objects(email="maazsabahuddin@gmail.com").first()
    user_data_obj = UserDTO(user.company_name, user.email)
    data = json.dumps(user_data_obj, default=dumper)
    if not user:
        return jsonify({
            'message': 'No data'
        })

    return Response(data, mimetype="application/json", status=200)


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
        id = user.id

        return jsonify({
            'status': status.HTTP_200_OK,
            'id': str(id),
            'message': 'User Added',
        })

    except Exception as e:
        return jsonify({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': str(e),
        })
