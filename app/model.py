from flask_sqlalchemy import SQLAlchemy
from flask import url_for
db = SQLAlchemy()


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(5000), nullable=True)
    image = db.Column(db.String(250), nullable=True)
    pages = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def image_url(self):
        return url_for("static", filename=f"uploads/{self.image}")

    @property
    def show_url(self):
        return url_for("books.show", id=self.id)

    @property
    def update_url(self):
        return url_for("books.update", id=self.id)

    @property
    def delete_url(self):
        return url_for("books.delete", id=self.id)
