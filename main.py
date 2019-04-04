from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def index():
	if request.method=='POST':
		return render_template('url.html',cevap=cevap)  
	else:
		return render_template('index.html')

if __name__ == "__main__":
    app.run()