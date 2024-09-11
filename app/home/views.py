from flask import render_template, request, redirect, url_for, Blueprint
from werkzeug.utils import secure_filename
import os, datetime

 
from app.model import db, Book

 
from app.home import home_blueprint


 
@home_blueprint.route("/", endpoint="home")
def home():
    books = Book.query.all() 
    return render_template("home.html", books=books)

 