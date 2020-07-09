bash stop-mycroft.sh all
msm update mycroft_bachelor_thesis.smilesmiley
msm remove mycroft-skill-version-checker
msm remove mycroft-hello-world.mycroft
cd mycroft/skills/mycroft_skill/
rm mycroft_skill.py
cd ../../client/speech/
rm listener.py
rm mic.py

cd ../../../

cp skills/mycroft_bachelor_thesis.smilesmiley/setup_one/mycroft_skill.py mycroft/skills/mycroft_skill/
cp skills/mycroft_bachelor_thesis.smilesmiley/mic.py mycroft/client/speech/
cp skills/mycroft_bachelor_thesis.smilesmiley/listener.py mycroft/client/speech/
bash start-mycroft.sh all
bash start-mycroft.sh cli
