import os
import phishing_detection
from flask import Flask
from flask import *
from werkzeug.utils import secure_filename
app = Flask(__name__)


@app.route('/result')
def result():
  urlname  = request.args['name']
  result  = phishing_detection.getResult(urlname)
  return result  


@app.route('/', methods = ['GET', 'POST'])
def hello():
	return  render_template("getInput.html")

if __name__ == '__main__':
  app.run(debug=True)
