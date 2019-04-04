from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
		return render_template('index.html')

@app.route("/sifrele")
def sifrele():
        return render_template('sifrele.html')

@app.route("/desifrele")
def desifrele():
    return render_template('desifre.html')

if __name__ == "__main__":
    app.run()