# temp_routes.py

from flask import Blueprint, redirect, render_template, url_for
from handler.temp_operation import *
from app.routes import api_routes
from app.models import *

main = Blueprint("main", __name__)


################################ Template routes ################################
@main.route("/")
def index():
    return "Welcome to the Portfolio CMS API!"


@main.route("/blog")
def blog():
    blogdata = Blog.query.order_by(Blog.id.desc()).all()
    return render_template("blog.html", blogdata=blogdata)


@main.route("/blog/create", methods=["POST"])
def create_blog():
    return handle_create(Blog, upload_folder="uploads", redirect_url="main.blog")


@main.route("/blog/edit/<int:id>", methods=["GET"])
def edit_blog(id):
    return handle_edit(Blog, id, redirect_url="blog.html")


@main.route("/blog/update/<int:id>", methods=["POST"])
def update_blog(id):
    return handle_update(Blog, id, upload_folder="uploads", redirect_url="main.blog")


@main.route("/blog/delete/<int:id>")
def delete_blog(id):
    return handle_delete(Blog, id, redirect_url="main.blog")
