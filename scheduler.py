#!/usr/bin/env python3
import schedule
import subprocess
import time
import os, shutil, stat
# https://janakiev.com/blog/python-background/
def job_two():
    # change to setup one
    # shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/setup_one/start.sh','./start.sh')
    # os.system('chmod 777 -R start.sh')
    # set permissions if not cannot execute
    stop =subprocess.call('./stop-mycroft.sh')
    # os.remove('mycroft/skills/mycroft_skill/mycroft_skill.py')
    # os.remove('/mycroft/client/speech/listener.py')
    # os.remove('/mycroft/client/speech/mic.py')
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/setup_two/mycroft_skill.py','./mycroft/skills/mycroft_skill/mycroft_skill.py')
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/mic.py','./mycroft/client/speech/mic.py')
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/listener.py','./mycroft/client/speech/listener.py')
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/weather/__init__.py','./skills/mycroft-weather.mycroftai/__init__.py')
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/joke/__init__.py','./skills/mycroft-joke.mycroftai/__init__.py')

    subprocess.call('./start-mycroft.sh')
    # to do do only once the job
    return schedule.CancelJob

def job_general():
    
    return schedule.CancelJob
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
schedule.every().day.at("15:27").do(job_two)
# schedule.every().day.at("12:56").do(job_script)

while 1:
    schedule.run_pending()
    time.sleep(1)