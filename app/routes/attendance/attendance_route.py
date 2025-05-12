from flask import Blueprint, jsonify, request
from app.services.attendance.attendance_service import get_attendance

attendance_bp = Blueprint('attendance', __name__, url_prefix='/api')

@attendance_bp.route('/attendance/get-attendance', methods=['GET'])
def get_attendance_route():
    return jsonify({'attendance': get_attendance()})