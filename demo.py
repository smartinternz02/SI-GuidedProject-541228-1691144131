from flask import Flask, url_for, redirect
app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return "LNCT College"

@app.route("/hello")
def hello():
    return"hello world"

@app.route("/hi")
def hi():
    return  "hello all faculty"

@app.route("/user/<enter>")
def user(enter):
    if enter =="welcome":
        return redirect (url_for("home"))
    elif enter =="hello":
        return redirect (url_for("hello"))
    else:
        return redirect (url_for("hi"))
if __name__ == "__main__":
    app.run(debug= True )