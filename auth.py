from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from __init__ import db

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        email = request.form.get("email")
        password = request.form.get("password")
        remember = True if request.form.get("remember") else False
        if not User.query.filter_by(email=email).first():
            flash("There's no account associated with that email. Please sign up.")
            return redirect(url_for("auth.signup"))
        elif not check_password_hash(
            User.query.filter_by(email=email).first().password, password
        ):
            flash("Incorrect password.")
            return redirect(url_for("auth.login"))
        login_user(User.query.filter_by(email=email).first(), remember=remember)
        return redirect(url_for("main.index"))


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        if User.query.filter_by(email=email).first():
            flash("Theres already an account with that email address")
        db.session.add(
            User(email=email, name=name, password=generate_password_hash(password))
        )
        db.session.commit()
        return redirect(url_for("auth.login"))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
