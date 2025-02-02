from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///anna.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db=SQLAlchemy(app)
app.app_context().push()

class Todo(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    desc=db.Column(db.String(500), nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self)->str:
        return f"{self.sno} - {self.title}"

@app.route("/")
def hello_world():
   todo=Todo(title="first todo",desc="description")
   db.session.add(todo)
   db.session.commit()
   alltodo=Todo.query.all()
   print(alltodo)
   return render_template("index.html",alltodo=alltodo)
    #return "<p>Hello, World!</p>"

@app.route("/show")
def show():
    alltodo=Todo.query.all()
    print(alltodo)
    return "<p>thhs is all todo page</p>"

if __name__ =="__main__":
    app.run(debug=True)
