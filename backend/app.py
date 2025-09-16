from dataclasses import fields

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from .config import Config
from .scheduler import init_scheduler
from .models import db
import traceback
from .meeting.routes import meeting_bp  # 从新蓝图文件导入

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(meeting_bp, url_prefix='/api')  # 注册会议室预定蓝图
CORS(app)  # 添加跨域支持

# 初始化定时任务调度器
scheduler = init_scheduler(app)

from .utils import validate_params

# 原装饰器已移至utils.py
def decorator(func):
    def wrapper(*args, **kwargs):
        data = request.get_json()
        missing = [field for field in fields if field not in data]
        if missing:
            return jsonify({'status': 'error', 'message': f'缺少必要参数: {missing}'}), 400
        return func(*args, **kwargs)
    return wrapper

# 删除以下重复的路由定义
# @app.route('/trigger-meeting', methods=['POST'])
# @validate_params(['roomId', 'startTime', 'endTime', 'userId'])
# def trigger_meeting():
#     try:
#         data = request.get_json()
#         room_id = data.get('roomId')
        
#         if not room_id:
#             return jsonify({
#                 'status': 'error',
#                 'message': '缺少会议室ID参数'
#             }), 400

#         # 此处添加实际业务逻辑
#         print(f"触发会议室 {room_id} 的会议")
        
#         return jsonify({
#             'status': 'success',
#             'message': '会议创建成功',
#             'roomId': room_id
#         }), 200

#     except Exception as e:
#         app.logger.error(f"接口异常: {str(e)}\n{traceback.format_exc()}")
#         return jsonify({
#             'status': 'error',
#             'message': '服务器内部错误',
#             'detail': str(e)
#         }), 500

# 添加应用实例导出
if __name__ == '__main__':
    app.run()

# 显式导出应用实例
app = app