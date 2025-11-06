# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from bst import BST, Node
from stack import Stack

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Initialize BST and Stack
bst = BST()
recent_stack = Stack(max_size=10)  # keep last 10 searches

# Sample data (optional)
sample_books = [
    (1001, "The Great Gatsby", "F. Scott Fitzgerald"),
    (1002, "To Kill a Mockingbird", "Harper Lee"),
    (1003, "1984", "George Orwell"),
    (1004, "Pride and Prejudice", "Jane Austen"),
]
for bid, title, author in sample_books:
    bst.insert(bid, title, author)


@app.route("/")
def index():
    books = bst.inorder()
    return render_template("index.html",books=books)

@app.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        try:
            book_id = int(request.form["book_id"])
            title = request.form["title"].strip()
            author = request.form["author"].strip()
            if not title or not author:
                flash("Title and Author cannot be empty.", "danger")
                return redirect(url_for("add_book"))
            if bst.search(book_id):
                flash(f"Book ID {book_id} already exists.", "warning")
            else:
                bst.insert(book_id, title, author)
                flash(f"Book {title} added successfully.", "success")
            return redirect(url_for("add_book"))
        except ValueError:
            flash("Book ID must be an integer.", "danger")
            return redirect(url_for("add_book"))
    return render_template("add.html")


@app.route("/search", methods=["GET", "POST"])
def search_book():
    book = None
    if request.method == "POST":
        try:
            book_id = int(request.form["book_id"])
            node = bst.search(book_id)
            if node:
                book = {"id": node.book_id, "title": node.title, "author": node.author}
                recent_stack.push(book)  # store recent search
                flash("Book found.", "success")
            else:
                flash("Book not found.", "warning")
        except ValueError:
            flash("Book ID must be an integer.", "danger")
    return render_template("search.html", book=book)


@app.route("/view_all")
def view_all():
    books = bst.inorder()
    return render_template("view_all.html", books=books)


@app.route("/delete", methods=["GET", "POST"])
def delete_book():
    if request.method == "POST":
        try:
            book_id = int(request.form["book_id"])
            if bst.search(book_id):
                bst.delete(book_id)
                flash(f"Book ID {book_id} deleted.", "success")
            else:
                flash("Book not found.", "warning")
            return redirect(url_for("delete_book"))
        except ValueError:
            flash("Book ID must be an integer.", "danger")
            return redirect(url_for("delete_book"))
    return render_template("delete.html")


@app.route("/recent")
def recent_books():
    books = recent_stack.items()
    return render_template("recent.html", books=books)


if __name__ == "__main__":
    app.run(debug=True)

# python3 app.py
