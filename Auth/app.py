from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register',method=['GET','POST'])
def register():
    if request.method == 'POST':
        #reuest handal
        pass   
    return render_template("register.html")

@app.route('/login',method=['GET','POST'])
def login():
    if request.method == 'POST':
        pass
    return render_template('login.html')
    



if __name__ == '__main__':
    app.run(debug=True)
    