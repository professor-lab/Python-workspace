from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///8anna.db"
db=SQLAlchemy(app)

class Todo(db.model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),primary_key=False)
    date_created=db.Column(db.DateTime,defaut=datetime.utcnow)

@app.route("/")
def hello_world():
   return render_template("index.html")
    #return "<p>Hello, World!</p>"

@app.route("/products")
def products():
    return "<p>thhs is products page</p>"

if __name__ =="__main__":
    app.run(debug=True)
