from flask import Flask, url_for, redirect, request, render_template
from jinja2 import Template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
     app.run( host='127.0.0.1', port='5000')             
debug = True