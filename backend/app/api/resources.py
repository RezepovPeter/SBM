from flask import Blueprint
from app.models import Resources
from app import db

resources = Blueprint('resources', __name__)

@resources.route('/', methods=['GET'])
def get_resources():
    resources = db.session.query(Resources).all()
    return "aboba"

@resources.route('/', methods=['POST'])
def add_resources():
    pass

@resources.route('/<int:id>', methods=['GET'])
def get_specific_resource(id):
    pass

@resources.route('/<int:id>', methods=['PATCH'])
def update_specific_resource(id):
    pass
