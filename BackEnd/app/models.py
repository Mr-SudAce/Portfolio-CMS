from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=True)
    is_active = db.Column(db.Boolean, default=True)
    is_staff = db.Column(db.Boolean, default=False)
    last_login = db.Column(db.DateTime, nullable=True)
    profile_image = db.Column(db.String(255), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    social_links = db.Column(db.Text, nullable=True)  # JSON string for social links
    contact_email = db.Column(db.String(150), nullable=True)
    phone_number = db.Column(db.String(20), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "is_admin": self.is_admin,
            "is_active": self.is_active,
            "is_staff": self.is_staff,
            "last_login": (
                self.last_login.strftime("%Y-%m-%d %H:%M:%S")
                if self.last_login
                else None
            ),
            "profile_image": self.profile_image,
            "bio": self.bio,
            "social_links": self.social_links,
            "contact_email": self.contact_email,
            "phone_number": self.phone_number,
            "location": self.location,
            "date_joined": self.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
            "created_on": self.created_on.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_on": self.updated_on.strftime("%Y-%m-%d %H:%M:%S"),
        }


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(300))
    github_link = db.Column(db.String(200))
    live_demo_link = db.Column(db.String(300))
    tech_stack = db.Column(db.String(200))
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "image": self.image,
            "github_link": self.github_link,
            "live_demo_link": self.live_demo_link,
            "tech_stack": self.tech_stack,
            "created_on": self.created_on.strftime("%Y-%m-%d %H:%M:%S"),
        }


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(100))
    icon = db.Column(db.String(255))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "level": self.level,
            "icon": self.icon,
        }


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(255), nullable=True)
    author = db.Column(db.String(100))
    tags = db.Column(db.String(200), nullable=True)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255), nullable=True)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "slug": self.slug,
            "author": self.author,
            "tags": self.tags.split(",") if self.tags else [],
            "content": self.content,
            "image": self.image,
            "created_on": self.created_on.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_on": self.updated_on.strftime("%Y-%m-%d %H:%M:%S"),
        }


class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    profile_image = db.Column(db.String(255))
    resume_link = db.Column(db.String(255))

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "profile_image": self.profile_image,
            "resume_link": self.resume_link,
        }


class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(150))  # Client, Instructor, etc.
    feedback = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255))  # Optional image

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "feedback": self.feedback,
            "image": self.image,
        }


class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100))
    start_date = db.Column(db.String(20))
    end_date = db.Column(db.String(20))
    description = db.Column(db.Text)
    location = db.Column(db.String(100))

    def serialize(self):
        return {
            "id": self.id,
            "company": self.company,
            "position": self.position,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "location": self.location,
        }


class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.String(100), nullable=False)
    degree = db.Column(db.String(100))
    field = db.Column(db.String(100))
    start_year = db.Column(db.String(10))
    end_year = db.Column(db.String(10))
    grade = db.Column(db.String(20))

    def serialize(self):
        return {
            "id": self.id,
            "school": self.school,
            "degree": self.degree,
            "field": self.field,
            "start_year": self.start_year,
            "end_year": self.end_year,
            "grade": self.grade,
        }


class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    subject = db.Column(db.String(200))
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "subject": self.subject,
            "message": self.message,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        }


class SocialLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(50))
    url = db.Column(db.String(255))
    icon = db.Column(db.String(100))
    order = db.Column(db.Integer, default=0)

    def serialize(self):
        return {
            "id": self.id,
            "platform": self.platform,
            "url": self.url,
            "icon": self.icon,
            "order": self.order,
        }
