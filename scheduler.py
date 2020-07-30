import schedule
import subprocess
import time

def job():
    subprocess.call('start.sh >/tmp/mycommand.log 2>&1')

    # to do do only once the job
    return schedule.CancelJob
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
schedule.every().day.at("20:07").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)