from flask import Blueprint, jsonify, request
from ..core import execute_meeting_requests
from ..scheduler import init_scheduler
from ..utils import validate_params

meeting_bp = Blueprint('meeting', __name__)

@meeting_bp.route('/trigger-meeting', methods=['POST'])
@validate_params(['roomId', 'startTime', 'endTime', 'userId'])
def handle_meeting():
    try:
        data = request.get_json()
        room_id = data['roomId']
        
        # 调用核心业务逻辑
        result = execute_meeting_request({
            'room_id': room_id,
            'start': data['startTime'],
            'end': data['endTime'],
            'user': data['userId']
        })

        return jsonify({
            'status': 'success' if result['status'] == 'success' else 'error',
            'message': '会议预定成功' if result['status'] == 'success' else '会议预定失败',
            'roomId': room_id
        }), 200

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': '服务器内部错误',
            'detail': str(e)
        }), 500