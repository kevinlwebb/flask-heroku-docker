from flask import render_template
from app import app, db
from app.models import Book

@app.before_first_request
def before_first_request():
    db.create_all()
    book = Book.query.filter_by(title='The Giver').first()
    if book is None:
        book = Book(
            title = "The Giver",
            author = "Lois Lowry"
            )
        db.session.add(book)
        db.session.commit()

@app.route('/')
def index():
    books = [{
        "title":book.title,
        "author":book.author
        } for book in Book.query.all()]
    return render_template('index.html', books=books)