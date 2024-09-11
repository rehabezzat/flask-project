from flask import render_template, request, redirect, url_for, Blueprint

from werkzeug.utils import secure_filename
import os, datetime


# db
from app.model import db, Book

# books
from app.books import books_blueprint
from app.books.forms import BooksForm


# =================================================================================================
# *** List Books ***
@books_blueprint.route("/", endpoint="list")
def books_list():
    books = Book.query.all()
    return render_template("book_list.html", books=books)


# =================================================================================================
# *** Create Books ***
@books_blueprint.route("create", endpoint="create", methods=["GET", "POST"])
def books_create():
    form = BooksForm()
    date = datetime.datetime.now()
    default_image = "default_image.jpg"

    if request.method == "POST":
        if form.validate_on_submit():
            con_name = default_image

            if request.files.get("image"):
                image = form.image.data
                image_name = secure_filename(image.filename)
                con_name = f"{date.day}-{date.hour}-{date.minute}-{image_name}"
                image.save(os.path.join("static/uploads/", con_name))

            data = dict(request.form)
            book = Book(
                name=data["name"],
                description=data["description"],
                image=con_name,
                pages=data["pages"],
                created_at=date,
        
            )

            db.session.add(book)
            db.session.commit()

            return redirect(book.show_url)
    return render_template("create_book.html", form=form)


# =================================================================================================
# *** Update Books ***
@books_blueprint.route("<int:id>/update", endpoint="update", methods=["GET", "POST"])
def books_update(id):
    book = db.get_or_404(Book, id)
    if book is None:
        return redirect(url_for("books.list"))
    form = BooksForm(obj=book)
    date = datetime.datetime.now()
    default_image = "default_image.jpg"

    if request.method == "POST":
        if form.validate_on_submit():
            con_name = book.image or default_image

            if form.image.data:
                image = form.image.data
                image_name = secure_filename(image.filename)
                con_name = f"{date.day}-{date.hour}-{date.minute}-{image_name}"
                image.save(os.path.join("static/uploads/", con_name))

            book.name = form.name.data
            book.description = form.description.data
            book.image = con_name
            book.pages = form.pages.data
            db.session.commit()

            return redirect(book.show_url)

    return render_template("edit_book.html", form=form, book=book)


# =================================================================================================
# *** Show Details Books ***
@books_blueprint.route("<int:id>", endpoint="show")
def book_show(id):
    book = db.get_or_404(Book, id)
    return render_template("book_detail.html", book=book)


# =================================================================================================
# *** Delete Books ***
@books_blueprint.route("<int:id>/delete", endpoint="delete", methods=["POST"])
def book_delete(id):
    book = db.get_or_404(Book, id)
    if book is None:
        return redirect(url_for("books.list"))
    default_image = "default_image.jpg"

    if book.image and book.image != default_image:
        image_path = os.path.join("static/uploads/", book.image)
        if os.path.exists(image_path):
            os.remove(image_path)

    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("books.list"))
