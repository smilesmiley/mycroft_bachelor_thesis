import schedule
import subprocess
import time
import os, shutil, stat

def job_copy():
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/setup_one/start.sh','./start.sh')
    # set permissions if not cannot execute
    # os.chmod("./start.sh",stat.S_IXUSR)
    subprocess.call('./start.sh')
    # to do do only once the job
    return schedule.CancelJob

def job_script():
    subprocess.call('./start.sh')
    return schedule.CancelJob
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
schedule.every().day.at("13:23").do(job_copy)
# schedule.every().day.at("12:56").do(job_script)

while 1:
    schedule.run_pending()
    time.sleep(1)