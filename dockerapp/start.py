from app import app, db
from app.models import Book


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Book': Book}

if __name__ == "__main__":
    app.run(debug=True, port=8000)
