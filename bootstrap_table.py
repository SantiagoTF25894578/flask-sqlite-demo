from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
app.app_context().push()

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="TREX21",
    password="4DrKUFLqu_LW_qA",  #psswd sin @
    hostname="TREX21.mysql.pythonanywhere-services.com",
    databasename="TREX21$user",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer, index=True)
    address = db.Column(db.String(256))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120), index=True)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    users = User.query
    return render_template('basic_table.html', title='Tabla ',
                           users=users)


if __name__ == '__main__':
    app.run()