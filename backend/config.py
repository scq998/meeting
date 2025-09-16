import os

class Config:
    API_KEY = os.getenv('MEETING_API_KEY', 'default_secret_key')
    MAX_RETRIES = 3
    RETRY_INTERVAL = 5  # 秒
    SCHEDULER_TIME = '09:59:59'
    THREAD_POOL_SIZE = 5
    
    # 数据库配置
    DB_HOST = 'm10778.mars.test.mysql.ljnode.com'
    DB_PORT = 10778
    DB_USER = 'root'
    DB_PASSWORD = 'Fa54D6a676'
    DB_NAME = 'huiju-tools'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False