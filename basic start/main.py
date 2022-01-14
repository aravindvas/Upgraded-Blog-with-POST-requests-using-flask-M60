from flask import Flask, render_template, request
import requests

# posts = requests.get("https://api.npoint.io/ec3c64c26e1ee4e3dc69").json()

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/loginA', methods=["POST"])
def data():
    name = request.form["usrname"]
    passd = request.form["usrpassword"]
    print(name, passd)
    return render_template("login.html", n=name, p=passd)

# @app.route('/loginA', methods=["POST"])
# def cnt():
#     name = request.form["usrname"]
#     passd = request.form["usrpassword"]
#     print(name, passd)
#     return f"Name: {name} Passd: {passd}"

if __name__ == "__main__" :
    app.run(debug=True, host="localhost")