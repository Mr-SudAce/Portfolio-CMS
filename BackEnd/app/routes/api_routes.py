# api_routes.py


from flask import Blueprint
from app.models import *
from app import db
from handler.api_operation import *

api = Blueprint("api", __name__)


################################ API routes ################################
# Create
# project
@api.route("/api/project", methods=["POST"])
def create_project():
    return handle_create(Project, upload_folder="uploads")


# skill
@api.route("/api/skill", methods=["POST"])
def create_skill():
    return handle_create(Skill)


# blog
@api.route("/api/blog", methods=["POST"])
def create_blog():
    return handle_create(Blog, upload_folder="uploads")


# Get all
# projects
@api.route("/api/projects", methods=["GET"])
def get_projects():
    return handle_get_all(Project)


# skills
@api.route("/api/skills", methods=["GET"])
def get_skills():
    return handle_get_all(Skill)


# blog posts
@api.route("/api/blogs", methods=["GET"])
def get_blogs():
    return handle_get_all(Blog)


# project Get by ID
@api.route("/api/project/get:<int:id>", methods=["GET"])
def get_project(id):
    return handle_get_one(Project, id)


# skill Get by ID
@api.route("/api/skill/get:<int:id>", methods=["GET"])
def get_skill(id):
    return handle_get_one(Skill, id)


# blog Get by ID
@api.route("/api/blog/get:<int:id>", methods=["GET"])
def get_blog(id):
    return handle_get_one(Blog, id)


# Update
# Project by ID
@api.route("/api/project/update/<int:id>", methods=["PUT"])
def update_project(id):
    return handle_update(Project, id, upload_folder="uploads")


# Skill by ID
@api.route("/api/skill/update/<int:id>", methods=["PUT"])
def update_skill(id):
    return handle_update(Skill, id, upload_folder="uploads")


# Blog by ID
@api.route("/api/blog/update/<int:id>", methods=["PUT"])
def update_blog(id):
    return handle_update(Blog, id, upload_folder="uploads")


# Delete
# project by ID
@api.route("/api/project/delete/<int:id>", methods=["DELETE"])
def delete_project(id):
    return handle_delete(Project, id)


# skill by ID
@api.route("/api/skill/delete/<int:id>", methods=["DELETE"])
def delete_skill(id):
    return handle_delete(Skill, id)


# blog by ID
@api.route("/api/blog/delete/<int:id>", methods=["DELETE"])
def delete_blog(id):
    return handle_delete(Blog, id)
