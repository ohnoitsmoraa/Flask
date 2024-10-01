from flask import Flask, make_response
from flask_migrate import Migrate
from model import db, User


# Creating an instance of flask app
app = Flask(__name__)

# Configuring the db to the local file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'

# Disable modification tracking to use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.json.compact = False

# Create a migrate object to manage schema modifications
migrate = Migrate(app, db)

# Initialize flask app to use the db
db.init_app(app)

@app.route('/')
def index():
    return 'Welcome to Flask!'

@app.route('/users/<username>')
def getUsername (username):
    return f'Welcome to flask development {username}'

@app.route('/users')
def getUsers():
    users = [{"id": user.id, "username": user.username, "email": user.email, "password": user.password, "age": user.age} for user in User.query.all()]
    # print(users)
    return make_response(users, 200)

if __name__ == '__main__':
    app.run(port=5500, debug=True)