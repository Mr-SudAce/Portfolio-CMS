# app/handlers/apihandler.py
from flask import jsonify, request
from app.models import db
import os
from werkzeug.utils import secure_filename


def handle_create(model, upload_folder):
    data = request.form.to_dict()
    file = request.files.get("image")
    try:
        if file:
            os.makedirs(upload_folder, exist_ok=True)
            filename = secure_filename(file.filename)
            filepath = os.path.join(upload_folder, filename)
            file.save(filepath)
            data["image"] = filename

        new_item = model(**data)
        db.session.add(new_item)
        db.session.commit()

        return (
            jsonify(
                {
                    "message": f"{model.__name__} created",
                    model.__name__: new_item.serialize(),
                }
            ),
            201,
        )

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


def handle_get_all(model):
    items = model.query.all()
    return jsonify({model.__name__: [item.serialize() for item in items]}), 200


def handle_get_one(model, id):
    item = model.query.get_or_404(id)
    return jsonify({model.__name__: item.serialize()}), 200


def handle_update(model, id, upload_folder):
    item = model.query.get_or_404(id)
    try:
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()

        file = request.files.get("image")
        if file and upload_folder:
            os.makedirs(upload_folder, exist_ok=True)

            filename = secure_filename(file.filename)
            filepath = os.path.join(upload_folder, filename)
            file.save(filepath)
            data["image"] = filename  # Save just filename in DB

        for key, value in data.items():
            setattr(item, key, value)
        db.session.commit()
        return (
            jsonify(
                {
                    "message": f"{model.__name__} updated",
                    model.__name__: item.serialize(),
                }
            ),
            200,
        )
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


def handle_delete(model, id):
    item = model.query.get_or_404(id)
    try:
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": f"{model.__name__} deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
