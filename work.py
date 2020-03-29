# For any query, contact maazsabahuddin@gmail.com
from flask import Flask
from User.db import initialize_db


from User.blueprint import my_view
app = Flask(__name__)
app.register_blueprint(my_view)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/Learn',
    'connect': False,
}
initialize_db(app)


if __name__ == "__main__":
    app.run(debug=True)
