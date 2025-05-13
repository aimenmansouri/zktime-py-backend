from flask import Blueprint, jsonify, request
from app.services.attendance.attendance_service import get_attendance

attendance_bp = Blueprint('attendance', __name__, url_prefix='/api')

@attendance_bp.route('/attendance/get-attendance', methods=['GET'])
def get_attendance_route():
    device_ip = request.args.get('device_ip', 'none')
    start_date = request.args.get('start_date', 'none')
    end_date = request.args.get('end_date', 'none')
    return jsonify({'attendance': get_attendance(device_ip , start_date , end_date )})