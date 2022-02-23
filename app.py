from crypt import methods
from flask import Flask, render_template, request, flash
import os
IMG_FOLDER = os.path.join('static', 'img')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

app.secret_key ="whatisyourname?"
@app.route("/hello")
def index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    flash("What is your name")
    return render_template("index.html")
    # , user_image = full_filename)
@app.route("/greet", methods=['POST', 'GET'])
def greet():
    flash("Hi " + str(request.form['name_input'])+ ", great to see you!")
    return render_template("index.html")