bash stop-mycroft.sh all
msm update mycroft-skill-addon.justfaked
msm remove mycroft-hello-world.mycroft
cd mycroft/skills/mycroft_skill/
rm mycroft_skill.py
cd ../../client/speech
rm listener.py
rm mic.py

cd ../../../

cp skills/mycroft-skill-addon.justfaked/mycroft_skill.py mycroft/skills/mycroft_skill/
cp skills/mycroft-skill-addon.justfaked/mic.py mycroft/client/speech/
cp skills/mycroft-skill-addon.justfaked/listener.py mycroft/client/speech/
bash start-mycroft.sh all
bash start-mycroft.sh cli
