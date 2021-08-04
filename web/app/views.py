import os
from flask import send_from_directory
from flask import render_template, flash, redirect, request, send_file
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
        title = 'Home')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
