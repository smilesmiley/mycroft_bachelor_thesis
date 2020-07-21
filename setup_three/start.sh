cd ../../../
bash stop-mycroft.sh all
msm update mycroft_bachelor_thesis.smilesmiley
msm update diary-skill.smilesmiley
msm remove mycroft-skill-version-checker
rm -rf skills/mycroft-date-time.mycroftai
rm -rf skills/mycroft-weather.mycroftai
rm -rf skills/mycroft-npr-news.mycroftai
rm -rf skills/mycroft-joke.mycroftai
msm install mycroft-weather.mycroftai
msm install mycroft-date-time.mycroftai
msm install mycroft-npr-news.mycroftai
msm install mycroft-joke.mycroftai
cd mycroft/skills/mycroft_skill/
rm mycroft_skill.py
cd ../../client/speech/
rm listener.py
rm mic.py

cd ../../../

cp skills/mycroft_bachelor_thesis.smilesmiley/setup_three/mycroft_skill.py mycroft/skills/mycroft_skill/
cp skills/mycroft_bachelor_thesis.smilesmiley/mic.py mycroft/client/speech/
cp skills/mycroft_bachelor_thesis.smilesmiley/listener.py mycroft/client/speech/

bash start-mycroft.sh all
bash start-mycroft.sh cli
