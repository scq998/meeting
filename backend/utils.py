from flask import jsonify, request

def validate_params(fields):
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = request.get_json()
            missing = [field for field in fields if field not in data]
            if missing:
                return jsonify({'status': 'error', 'message': f'缺少必要参数: {missing}'}), 400
            return func(*args, **kwargs)
        return wrapper
    return decorator