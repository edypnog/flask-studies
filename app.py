from flask import Flask, g, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


# Database Connection Functions
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(":memory:")  # Use in-memory database
        g.db.row_factory = sqlite3.Row
        init_db()  # Initialize the database with the schema
    return g.db


# Database Initialization
def init_db():
    conn = get_db()
    with app.open_resource("schema.sql", mode="r") as f:
        conn.cursor().executescript(f.read())
    conn.commit()


# Routes for CRUD operations


@app.route("/")
def index():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return render_template("index.html", books=books)


@app.route("/add", methods=["POST"])
def add_book():
    title = request.form["title"]
    author = request.form["author"]

    conn = get_db()
    conn.execute(
        "INSERT INTO books (title, author) VALUES (?, ?)", (title, author)
    )  # pylint: disable=protected-access
    conn.commit()
    conn.close()

    return redirect(url_for("index"))


@app.route("/edit/<int:book_id>")
def edit_book(book_id):
    conn = get_db()
    cursor = conn.execute("SELECT * FROM books WHERE id=?", (book_id,))
    book = cursor.fetchone()
    conn.close()

    if book:
        return render_template("edit.html", book=book)
    else:
        return "Book not found."


@app.route("/update/<int:book_id>", methods=["POST"])
def update_book(book_id):
    title = request.form["title"]
    author = request.form["author"]

    conn = get_db()
    conn.execute(
        "UPDATE books SET title=?, author=? WHERE id=?",
        (title, author, book_id),  # pylint: disable=protected-access
    )
    conn.commit()
    conn.close()

    return redirect(url_for("index"))


@app.route("/delete/<int:book_id>")
def delete_book(book_id):
    conn = get_db()
    conn.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True, use_reloader=True)
