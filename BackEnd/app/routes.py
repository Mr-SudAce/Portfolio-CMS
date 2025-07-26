from flask import Blueprint, render_template, request, jsonify
from app.models import *
from app import db
from handler.apihandler import *

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return "Welcome to the Portfolio CMS API!"

@main.route("/blog")
def blog():
    return render_template("blog.html")

# Create
# project
@main.route("/api/project", methods=["POST"])
def create_project():
    return handle_create(Project, upload_folder="uploads")


# skill
@main.route("/api/skill", methods=["POST"])
def create_skill():
    return handle_create(Skill)


# blog
@main.route("/api/blog", methods=["POST"])
def create_blog():
    return handle_create(Blog, upload_folder="uploads")


# Get all
# projects
@main.route("/api/projects", methods=["GET"])
def get_projects():
    return handle_read_all(Project)


# skills
@main.route("/api/skills", methods=["GET"])
def get_skills():
    return handle_read_all(Skill)

# blog posts
@main.route("/api/blogs", methods=["GET"])
def get_blogs():
    return handle_read_all(Blog)










# project Get by ID
@main.route("/api/project/get:<int:id>", methods=["GET"])
def get_project(id):
    return handle_read_one(Project, id)


# skill Get by ID
@main.route("/api/skill/get:<int:id>", methods=["GET"])
def get_skill(id):
    return handle_read_one(Skill, id)

# blog Get by ID
@main.route("/api/blog/get:<int:id>", methods=["GET"])
def get_blog(id):
    return handle_read_one(Blog, id)












# Update
# Project by ID
@main.route("/api/project/update:<int:id>", methods=["PUT"])
def update_project(id):
    return handle_update(Project, id)


# Skill by ID
@main.route("/api/skill/update:<int:id>", methods=["PUT"])
def update_skill(id):
    return handle_update(Skill, id)

# Blog by ID
@main.route("/api/blog/update:<int:id>", methods=["PUT"])
def update_blog(id):
    return handle_update(Blog, id)




# Delete
# project by ID
@main.route("/api/project/delete:<int:id>", methods=["DELETE"])
def delete_project(id):
    return handle_delete(Project, id)


# skill by ID
@main.route("/api/skill/delete:<int:id>", methods=["DELETE"])
def delete_skill(id):
    return handle_delete(Skill, id)


# blog by ID
@main.route("/api/blog/delete:<int:id>", methods=["DELETE"])
def delete_blog(id):
    return handle_delete(Blog, id)
