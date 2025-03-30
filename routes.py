from flask import Blueprint, jsonify, request
from app.models import YourModel  # Replace with your actual model
from app import db

bp = Blueprint('main', __name__)

@bp.route('/your_endpoint', methods=['GET'])
def get_items():
    items = YourModel.query.all()
    return jsonify([item.to_dict() for item in items])  # Ensure to implement to_dict method in your model

@bp.route('/your_endpoint', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = YourModel(**data)  # Ensure your model can accept these fields
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201  # Ensure to implement to_dict method in your model

@bp.route('/your_endpoint/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = YourModel.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204  # No content response for successful deletion