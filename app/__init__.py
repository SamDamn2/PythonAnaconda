from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)


    from app.routes import fruta_routes, tfrutha_routes
    app.register_blueprint(tfrutha_routes.bp)
    app.register_blueprint(fruta_routes.bp)

    return app