from flask import Blueprint, request, jsonify
from app.models import *
from app import db

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return "Welcome to the Portfolio CMS API!"


# Get all
# projects
@main.route("/api/projects", methods=["GET"])
def get_projects():
    projects = Project.query.all()
    return (
        jsonify(
            {
                "message": "Projects retrieved successfully",
                "projects": [
                    {
                        "id": project.id,
                        "title": project.title,
                        "description": project.description,
                        "image": project.image,
                        "link": project.link,
                    }
                    for project in projects
                ],
            }
        ),
        200,
    )


# skills
@main.route("/api/skills", methods=["GET"])
def get_skills():
    skills = Skill.query.all()
    return (
        jsonify(
            {
                "message": "Skills retrieved successfully",
                "skills": [
                    {
                        "id": skill.id,
                        "name": skill.name,
                        "level": skill.level,
                        "category": skill.category,
                        "icon": skill.icon,
                    }
                    for skill in skills
                ],
            }
        ),
        200,
    )


# Get by ID
# project
@main.route("/api/project/get:<int:id>", methods=["GET"])
def get_project(id):
    project = Project.query.get_or_404(id)
    return (
        jsonify(
            {
                "id": project.id,
                "title": project.title,
                "description": project.description,
                "image": project.image,
                "link": project.link,
            }
        ),
        200,
    )


# skill
@main.route("/api/skill/get:<int:id>", methods=["GET"])
def get_skill(id):
    skill = Skill.query.get_or_404(id)
    return (
        jsonify(
            {
                "id": skill.id,
                "name": skill.name,
                "level": skill.level,
                "category": skill.category,
                "icon": skill.icon,
            }
        ),
        200,
    )


# Create 
# project
@main.route("/api/project", methods=["POST"])
def create_project():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    project = Project(
        title=data["title"],
        description=data.get("description"),
        image=data.get("image"),
        link=data.get("link"),
    )
    db.session.add(project)
    db.session.commit()

    return jsonify({"message": "Project created", "id": project.id}), 201


# skill
@main.route("/api/skill", methods=["POST"])
def create_skill():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    skill = Skill(
        name=data["name"],
        level=data.get("level"),
        category=data.get("category"),
        icon=data.get("icon"),
    )
    db.session.add(skill)
    db.session.commit()

    return jsonify({"message": "Skill created", "id": skill.id}), 201


# Update 
# Project by ID
@main.route("/api/project/update:<int:id>", methods=["PUT"])
def update_project(id):
    project = Project.query.get_or_404(id)
    data = request.get_json()

    project.title = data.get("title", project.title)
    project.description = data.get("description", project.description)
    project.image = data.get("image", project.image)
    project.link = data.get("link", project.link)
    db.session.commit()
    return jsonify({"message": "Project updated!"})


# Skill by ID
@main.route("/api/skill/update:<int:id>", methods=["PUT"])
def update_skill(id):
    skill = Skill.query.get_or_404(id)
    data = request.get_json()

    skill.name = data.get("name", skill.name)
    skill.level = data.get("level", skill.level)
    skill.category = data.get("category", skill.category)
    skill.icon = data.get("icon", skill.icon)

    db.session.commit()

    return jsonify({"message": "Skill updated"}), 200


# Delete 
# project by ID
@main.route("/api/project/delete:<int:id>", methods=["DELETE"])
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({"message": "Project deleted!"})


# skill by ID
@main.route("/api/skill/delete:<int:id>", methods=["DELETE"])
def delete_skill(id):
    skill = Skill.query.get_or_404(id)
    db.session.delete(skill)
    db.session.commit()
    return jsonify({"message": "Skill deleted"}), 200
