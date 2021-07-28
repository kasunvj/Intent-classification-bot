import urllib
import json
import os
from flask import Flask , render_template, request,make_response
app = Flask(__name__)

@app.route("/getvoice", methods=['POST'])
def getvoice():
	if request.method == 'POST':
		req = request.get_json(silent = True, force = True)
		print(req)
	return "<h1>Fuck GB</h1>"


@app.route("/home")
def hello():
	return render_template('home.html')

@app.route("/about")
def about():
	return "<h1>About the world</h1>"

if __name__  == '__main__':
	app.run(debug=True)