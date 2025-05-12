from flask import Blueprint, jsonify, request
from app.services.example_service import say_hello

example_bp = Blueprint('example', __name__, url_prefix='/api')

@example_bp.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', 'persone')
    return jsonify({'message': say_hello(name)})