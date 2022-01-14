from flask import Flask, render_template, request
import requests
import smtplib


posts = requests.get("https://api.npoint.io/ec3c64c26e1ee4e3dc69").json()

tomail = "mailme.anonymous.1@gmail.com"
pswd = "mailme1997"

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html", alp=posts)

@app.route('/about')
def abt():
    return render_template("about.html")

@app.route('/contact', methods=["GET", "POST"] )
def cnt():
    if request.method == "POST":
        dt = request.form
        print(dt["name"])
        print(dt["email"])
        print(dt["phone"])
        print(dt["message"])
        snt_ml(dt["name"], dt["email"], dt["phone"], dt["message"])
        # return "<h1>Successfully sent your message</h1>"
        return render_template("contact.html", snt=True)
    return render_template("contact.html", snt=False)

def snt_ml(nm, ml, pn, msg):
    em_msg = f"Subject:Blog Message\n\nName: {nm}\nMail: {ml}\nPhone: {pn}\n Mesage: {msg}"
    with smtplib.SMTP("smtp.gmail.com:587") as conn:
        conn.starttls()
        conn.ehlo()
        conn.login(tomail, pswd)
        conn.sendmail(from_addr=tomail, to_addrs=tomail, msg=em_msg)

@app.route('/post/<int:index>')
def pst(index):
    req_pst = None
    for bp in posts:
        if bp["id"] == index:
            req_pst = bp
    return render_template("post.html", p2=req_pst)


if __name__ == "__main__" :
    app.run(debug=True, host="localhost")