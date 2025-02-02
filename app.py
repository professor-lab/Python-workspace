from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/products")
def products():
    return "<p>thhs is products page</p>"

if __name__ =="__main__":
    app.run(debug=True)
