bash stop-mycroft.sh all
msm update mycroft_bachelor_thesis.smilesmiley
msm remove mycroft-skill-version-checker

cd mycroft/skills/mycroft_skill/
rm mycroft_skill.py
cd ../../client/speech/
rm listener.py
rm mic.py

cd ../../../

cp skills/mycroft_bachelor_thesis.smilesmiley/setup_one/mycroft_skill.py mycroft/skills/mycroft_skill/
cp skills/mycroft_bachelor_thesis.smilesmiley/mic.py mycroft/client/speech/
cp skills/mycroft_bachelor_thesis.smilesmiley/listener.py mycroft/client/speech/
rm skills/mycroft-weather.mycroftai/__init__.py
cp skills/mycroft_bachelor_thesis.smilesmiley/weather/__init__.py skills/mycroft-weather.mycroftai/
rm skills/mycroft-joke.mycroftai/__init__.py
cp skills/mycroft_bachelor_thesis.smilesmiley/joke/__init__.py skills/mycroft-joke.mycroftai/
rm skills/mycroft-npr-news.mycroftai/__init__.py
cp skills/mycroft_bachelor_thesis.smilesmiley/news/__init__.py skills/mycroft-npr-news.mycroftai/

bash start-mycroft.sh all
bash start-mycroft.sh cli
