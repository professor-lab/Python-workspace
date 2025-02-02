from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
   return render_template("index.html")
    #return "<p>Hello, World!</p>"

@app.route("/products")
def products():
    return "<p>thhs is products page</p>"

if __name__ =="__main__":
    app.run(debug=True)
