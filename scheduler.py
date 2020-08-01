import schedule
import subprocess
import time
import os, shutil

def job():
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/setup_one/start.sh','./')
    subprocess.call('start.sh')

    # to do do only once the job
    return schedule.CancelJob
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
schedule.every().day.at("12:34").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)