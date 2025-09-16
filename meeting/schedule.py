from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import yuding_1
from meeting import yuding_2, yuding_3


def task():
    now = datetime.now()
    ts = now.strftime("%Y-%m-%d %H:%M:%S")
    print(ts)


def task2():
    now = datetime.now()
    ts = now.strftime("%Y-%m-%d %H:%M:%S")
    print(ts + ' 666!')


def task3():
    yuding_1.yuding()


def task4():
    yuding_2.yuding()


def task5():
    yuding_3.yuding()


def func():
    # 创建调度器BlockingScheduler()
    scheduler = BlockingScheduler()
    # scheduler.add_job(task, 'interval', seconds=0, id='test_job1')
    # # 添加任务，时间间隔为5秒
    # scheduler.add_job(task2, 'interval', seconds=0, id='test_job2')
    # 在2022-10-27 21:50:30和2022-10-27 21:51:30之间，时间间隔为6秒
    # scheduler.add_job(task3, 'interval', seconds=0, start_date='2024-8-19 09:59:59', end_date='2024-8-19 10:00:02',
    #                   id='test_job3')
    # scheduler.add_job(task4, 'interval', seconds=0, start_date='2024-8-19 09:59:59', end_date='2024-8-19 10:00:02',
    #                   id='test_job4')

    scheduler.add_job(task3, 'interval', seconds=0, start_date='2024-8-22 09:59:58', end_date='2024-8-22 10:30:02',
                      id='test_job3')
    scheduler.add_job(task4, 'interval', seconds=0, start_date='2024-8-22 09:59:58', end_date='2024-8-22 10:30:02',
                      id='test_job4')

    scheduler.add_job(task5, 'interval', seconds=0, start_date='2024-8-22 09:59:58', end_date='2024-8-22 10:30:02',
                      id='test_job5')
    # 每小时（上下浮动20秒区间内）运行task
    # jitter振动参数，给每次触发添加一个随机浮动秒数，一般适用于多服务器，避免同时运行造成服务拥堵。
    # scheduler.add_job(task, 'interval', hours=1, jitter=20, id='test_job4')
    scheduler.start()


func()
