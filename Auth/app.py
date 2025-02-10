from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import bcrypt


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100),unique=True)
    password=db.Column(db.string(100))

    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=bcrypt.haspw(password.encode('utf-8'),bcrypt.getsalt()).decode('utf-8')
       

    def check_password(self,password):
        return bcrypt.chekpw(password.encod('utf-8'),self.password.encode('utf-8'))

with app.app_context():
    db.create_all()   



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        #reuest handal
        pass   
    return render_template("register.html")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        pass
    return render_template('login.html')
    



if __name__ == '__main__':
    app.run(debug=True)
    