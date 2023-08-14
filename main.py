from flask import Flask, render_template, request, redirect, url_for, session, send_file, flash, jsonify

app = Flask(__name__)

@app.route("/home",methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")

