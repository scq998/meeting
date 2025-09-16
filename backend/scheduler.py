from apscheduler.schedulers.background import BackgroundScheduler
from .core import execute_meeting_requests
from .config import Config


def init_scheduler(app):
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        id='daily_meeting_task',
        func=execute_meeting_requests,
        trigger='cron',
        hour=Config.SCHEDULER_TIME.split(':')[0],
        minute=Config.SCHEDULER_TIME.split(':')[1],
        second=Config.SCHEDULER_TIME.split(':')[2]
    )
    scheduler.start()
    return scheduler