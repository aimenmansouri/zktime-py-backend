from flask import Blueprint, jsonify, request
from app.services.attendance.users_service import get_users

users_bp = Blueprint('users', __name__, url_prefix='/api')

@users_bp.route('/attendance/get-users', methods=['GET'])
def get_users_route():
    device_ip = request.args.get('device_ip', 'none')
    return jsonify({'users': get_users(device_ip)})