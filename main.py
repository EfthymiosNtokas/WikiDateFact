from flask import Flask, render_template, request, redirect, url_for, session, send_file, flash, jsonify
import datetime
from wikiscraper import WikiScraper
from wikisearcher import WikiSearcher
from htmlgetter import HtmlGetter


app = Flask(__name__)


def makestring(mo, d):
    months_camel = {
        1: "january",
        2: "february",
        3: "march",
        4: "april",
        5: "may",
        6: "june",
        7: "july",
        8: "august",
        9: "september",
        10: "october",
        11: "november",
        12: "december"
    }
    ans = months_camel[int(mo)]+" "
    ans+=str(d)
    digit = int(d)%10
    if digit==0 or digit>3: ans+="th"
    elif digit ==1: ans+="st"
    elif digit==2: ans+="nd"
    else: ans+="rd"
    return ans


def dodate(d):
    return '12'


def dotoday():
    date = datetime.datetime.today()
    mo = date.month
    d = date.day  # call function that makes the string
    s = makestring(mo,d)
    print(s)
    return '231'


def dorandom():
    return '321'


@app.route("/home", methods=['GET', 'POST'])
def home():

    print(request.form)
    quote = ""
    if 'random' in request.form:
        quote = dorandom()
    elif 'today' in request.form:
        quote = dotoday()
    elif 'date' in request.form:
        quote = dodate(request.form['date'])
    date = datetime.datetime.today()
    print(date.month)
    print(date.day)

    return render_template("home.html", quote=quote)
