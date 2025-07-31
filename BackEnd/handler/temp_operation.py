from app.models import db

from flask import redirect, render_template, request, jsonify, url_for
from werkzeug.utils import secure_filename
import os


def handle_create(model, upload_folder=None, redirect_url=None):
    if request.method == "POST":
        data = request.form.to_dict()
        if upload_folder:
            file = request.files.get("image")
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(upload_folder, filename))
                data["image"] = filename
        new_entry = model(**data)
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for(redirect_url))

def handle_edit(model, id, redirect_url=None):
    blog = model.query.get_or_404(id)
    blogdata = model.query.all()  # if you need all for the bottom list
    return render_template(redirect_url, blog=blog, blogdata=blogdata)

def handle_update(model, id, upload_folder=None, redirect_url=None):
    if request.method == "POST":
        data = request.form.to_dict()
        if upload_folder:
            file = request.files.get("image")
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(upload_folder, filename))
                data["image"] = filename
        model.query.filter_by(id=id).update(data)
        db.session.commit()
        return redirect(url_for(redirect_url))


def handle_delete(model, id, redirect_url=None):
    blog = model.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for(redirect_url))
