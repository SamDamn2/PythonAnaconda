from flask import Blueprint

bp = Blueprint('main', __name__)

from app.routes import fruta_routes, tfrutha_routes