#!/bin/bash

source .venv/bin/activate
bash stop-mycroft.sh all
msm update mycroft_bachelor_thesis.smilesmiley
msm remove mycroft-skill-version-checker
msm update diary-skill.smilesmiley
rm ./mycroft/skills/mycroft_skill/mycroft_skill.py

rm ./mycroft/client/speech/listener.py
rm ./mycroft/client/speech/mic.py

cp ./skills/mycroft_bachelor_thesis.smilesmiley/setup_one/mycroft_skill.py ./mycroft/skills/mycroft_skill/
cp ./skills/mycroft_bachelor_thesis.smilesmiley/mic.py ./mycroft/client/speech/
cp ./skills/mycroft_bachelor_thesis.smilesmiley/listener.py ./mycroft/client/speech/
rm ./skills/mycroft-weather.mycroftai/__init__.py
cp ./skills/mycroft_bachelor_thesis.smilesmiley/weather/__init__.py ./skills/mycroft-weather.mycroftai/
rm ./skills/mycroft-joke.mycroftai/__init__.py
cp ./skills/mycroft_bachelor_thesis.smilesmiley/joke/__init__.py ./skills/mycroft-joke.mycroftai/
rm ./skills/mycroft-npr-news.mycroftai/__init__.py
cp ./skills/mycroft_bachelor_thesis.smilesmiley/news/__init__.py ./skills/mycroft-npr-news.mycroftai/
rm ./skills/mycroft-date-time.mycroftai/__init__.py
cp ./skills/mycroft_bachelor_thesis.smilesmiley/date/__init__.py ./skills/mycroft-date-time.mycroftai/
bash start-mycroft.sh all
bash start-mycroft.sh cli

