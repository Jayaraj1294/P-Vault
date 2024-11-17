from flask import Flask, Blueprint, render_template, request
from app.strength.pass_check import *

strength = Blueprint("strength", __name__)

@strength.route("/")
def display():
    return render_template('strength.html')


@strength.route("/tools/check_strength", methods=['GET','POST'])
def check_strength(sum=""):
    if request.method == 'POST':
        password = request.form['pwd']
        x.append(password)
        ip = vectorizer.fit_transform(x)
        switcher = {
            0: "Weak password!!!",
            1: "Moderate password!!!",
            2: "Strong password!!!",
        }
        ans = m.predict(ip)
        return render_template('strength.html', sum=switcher.get(ans[-1], " "))

    else:
        return render_template('strength.html', sum=" ")