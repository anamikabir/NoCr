import time
import atexit
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

# Sample schedular app 
def send_notifications():
    print time.strftime("%A, %d. %B %Y %I:%M:%S %p")

def del_old_contents():
    print "Running second job at a different interval"

app = Flask(__name__)

scheduler = BackgroundScheduler()
#scheduler.start()
scheduler.add_job(
    func=send_notifications,
    trigger=IntervalTrigger(seconds=10),
    id='notification_job',
    name='Send notification for new posts every 30 mins',
    replace_existing=True)

scheduler.add_job(
    func=del_old_contents,
    trigger=IntervalTrigger(seconds=15),
    id='del_old_dict_job',
    name='Delete older post enteries - runs once every 24 hours',
    replace_existing=True)

scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


if __name__ == '__main__':
    app.run()
