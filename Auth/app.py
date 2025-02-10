from flask import Flask, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import bcrypt


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100),unique=True)
    password=db.Column(db.String(100))

    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
       

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
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']

        new_user=User(name=name,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('login')
        #reuest handal
        pass   
    return render_template("register.html")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']

        user=User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session['name']=user.name
            session['email']=user.email
            session['password']=user.password
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='invalid user')
              
    return render_template('login.html')
@app.route('/dashboard')
def dashboard():
    if session['name']:
        return render_template('dashboard.html')
    return redirect('/login')
    



if __name__ == '__main__':
    app.run(debug=True)
    