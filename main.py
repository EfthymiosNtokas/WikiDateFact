from flask import Flask, render_template, request, redirect, url_for, session, send_file, flash, jsonify
import datetime
from wikiscraper import WikiScraper
from wikisearcher import WikiSearcher
from htmlgetter import HtmlGetter
import random


app = Flask(__name__)
def random_date(start, end):
  return start + datetime.timedelta(
      seconds=random.randint(0, int((end - start).total_seconds())))

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
    a = d.split('-')
    mo = a[1]
    da=a[2]
    s=makestring(mo, da)
    
    return s


def dotoday():
    date = datetime.datetime.today()
    mo = date.month
    d = date.day  # call function that makes the string
    s = makestring(mo,d)
    print(s)
    return s


def dorandom():
    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime(2025, 1, 1)
    date= random_date(start, end)
    mo = str(date.month)
    d = str(date.day)
    s=makestring(mo, d)
    print(s)
    print(d)
    return s


@app.route("/home", methods=['GET', 'POST'])
def home():

    print(request.form)
    quote = ""
    date=""
    if 'random' in request.form:
        date = dorandom()
    elif 'today' in request.form:
        date = dotoday()
    elif 'date' in request.form:
        date = dodate(request.form['date'])
    if date!= "":
        wiki = WikiSearcher(date) #get 1 page id
        page1 = wiki.get_pages(20)[0]
        w = WikiScraper(page1) #scrape it
        info = w.get_content()
        obj = HtmlGetter(info) #get one bullet
        quote=obj.random_bullet()
    

    return render_template("home.html", date=date, quote=quote)
@app.route('/')
def root():
    return redirect(url_for('home'))

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('home'))
