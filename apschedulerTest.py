from datetime import datetime

from apscheduler.schedulers.background import BlockingScheduler

scheduler = BlockingScheduler()

def job_function():
    print("Hello World")


scheduler.add_job(job_function, 'interval', seconds=0.01)

scheduler.start()