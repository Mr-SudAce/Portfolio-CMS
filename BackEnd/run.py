from flask_migrate import upgrade
from app import create_app, db

app = create_app()





def auto_migrate():
    try:
        upgrade()
        print("✅ Database schema is up to date.")
    except Exception as e:
        print("❌ Migration failed:", e)


if __name__ == "__main__":
    with app.app_context():
        auto_migrate()
    app.run(debug=True)
