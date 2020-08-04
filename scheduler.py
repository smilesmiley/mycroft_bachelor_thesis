#!/usr/bin/env python3
import schedule
import subprocess
import time
import os, shutil, stat
# https://janakiev.com/blog/python-background/
def job_one():

    # change to setup one
    # shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/setup_one/start.sh','./start.sh')
    # os.system('chmod 777 -R start.sh')
    # set permissions if not cannot execute
    subprocess.call('./stop-mycroft.sh')
    # os.remove('mycroft/skills/mycroft_skill/mycroft_skill.py')
    # os.remove('/mycroft/client/speech/listener.py')
    # os.remove('/mycroft/client/speech/mic.py')
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/setup_one/mycroft_skill.py','./mycroft/skills/mycroft_skill/mycroft_skill.py')
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/mic.py','./mycroft/client/speech/mic.py')
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/listener.py','./mycroft/client/speech/listener.py')
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/weather/__init__.py','./skills/mycroft-weather.mycroftai/__init__.py')
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/joke/__init__.py','./skills/mycroft-joke.mycroftai/__init__.py')

    subprocess.call('./start-mycroft.sh')
    time.sleep(10)
    # to do do only once the job


def job_two():

    subprocess.call('./stop-mycroft.sh')
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/setup_two/mycroft_skill.py','./mycroft/skills/mycroft_skill/mycroft_skill.py')
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/mic.py','./mycroft/client/speech/mic.py')
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/listener.py','./mycroft/client/speech/listener.py')
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/weather/__init__.py','./skills/mycroft-weather.mycroftai/__init__.py')
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/joke/__init__.py','./skills/mycroft-joke.mycroftai/__init__.py')

    subprocess.call('./start-mycroft.sh')
    time.sleep(10)
    # to do do only once the job


def job_three():
    subprocess.call('./stop-mycroft.sh')
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/setup_three/weather/__init__.py','./skills/mycroft-weather.mycroftai/__init__.py')
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/setup_three/joke/__init__.py','./skills/mycroft-joke.mycroftai/__init__.py')
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/setup_three/mycroft_skill.py','./mycroft/skills/mycroft_skill/mycroft_skill.py')
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/mic.py','./mycroft/client/speech/mic.py')
    shutil.copy('skills/mycroft_bachelor_thesis.smilesmiley/listener.py','./mycroft/client/speech/listener.py')

# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
schedule.every().day.at("17:55").do(job_two)
# schedule.every().wednesday.at("8:00").do(job_one)
# schedule.every().thursday.at("8:00").do(job_two)
# schedule.every().friday.at("8:00").do(job_three)

while 1:
    schedule.run_pending()
    time.sleep(1)