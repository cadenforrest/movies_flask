from flask import Blueprint, Flask, render_template, request, jsonify, flash
from flask_login.utils import login_required
from __init__ import create_app, db
from models import User, Movie
from create_movies_db import create_movies_db
from os.path import exists

main = Blueprint("main", __name__)


@main.route("/profile")
def profile():
    return render_template("profile.html")


@main.route("/")
@login_required
def index():
    return render_template("table.html", title="Searchable Movies!")


@main.route("/api/data")
def data():
    query = Movie.query
    search = request.args.get("search[value]")
    if search:
        query = query.filter(
            db.or_(
                Movie.title.like(f"%{search}%"),
            )
        )
    total_filtered = query.count()

    order = []
    i = 0
    while True:
        col_index = request.args.get(f"order[{i}][column]")
        if col_index is None:
            break
        col_title = request.args.get(f"columns[{col_index}][data]")
        if col_title not in ["title", "year"]:
            col_title = "title"
        descending = request.args.get(f"order[{i}][dir]") == "desc"
        col = getattr(Movie, col_title)
        if descending:
            col = col.desc()
        order.append(col)
        i += 1
    if order:
        query = query.order_by(*order)
    start = request.args.get("start", type=int)
    length = request.args.get("length", type=int)
    query = query.offset(start).limit(length)
    return jsonify(
        {
            "data": [movie.to_dict() for movie in query],
            "recordsFiltered": total_filtered,
            "recordsTotal": Movie.query.count(),
            "draw": request.args.get("draw", type=int),
        }
    )


app = create_app()
if __name__ == "__main__":
    if not exists("db.sqlite"):
        with app.app_context():
            db.create_all(app=create_app())
            create_movies_db()
    app.run(debug=True)
