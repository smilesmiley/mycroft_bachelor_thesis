# mycroft-skill-addon
Enhancements for mycroft-skills to conduct user-centric studies.

# Contents
* [About](#about)
* [Setup](#setup)
* [Components](#components)
* [Run the Example](#run-the-example)
* [Credits](#credits)

# About
Our goal is to perform user studies with a smart speaker called Mycroft. Therefore, we overwrite the main classes of Mycroft. This repository contains all need files to conduct a user study with a specific skill.

# Setup
* Setup and pair your device by following the official documentation: ```https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/get-mycroft```
* Installing our skill by executing the following terminal command: ```msm install https://github.com/justfaked/mycroft-skill-addon.git```
* Navigate to the ``mycroft-core/`` folder and use the command ``$ git reset --hard d49ca6d41`` 
> Currently the survey only supports mycroft-versions 19.x.x
* Navigate to ```\mycroft-core\mycroft\skills\mycroft-skill-addon.justfaked\``` and move the included ```start.sh``` script into the ```\mycroft-core\``` folder.
* Execute the script via the command ```$ bash start.sh```
* Modify all skills that shall be included in the user study
* Reboot the device

# Integrate Study into Skill
* Insert following code snippet at the end of each IntentHandler(which should trigger the study) of the SKill class:


# Components

## start.sh
````
bash stop-mycroft.sh all
msm update mycroft-skill-addon.justfaked
msm remove mycroft-hello-world.mycroft
cd mycroft/skills/mycroft_skill/
rm mycroft_skill.py
cd ../../client/speech/
rm listener.py
rm mic.py
cd ../../../
cp skills/mycroft-skill-addon.justfaked/mycroft_skill.py mycroft/skills/mycroft_skill/
cp skills/mycroft-skill-addon.justfaked/mic.py mycroft/client/speech/
cp skills/mycroft-skill-addon.justfaked/listener.py mycroft/client/speech/
bash start-mycroft.sh all
bash start-mycroft.sh cli
````

This script keeps the survey functionality up-to-date and removes conflicting files. It replaces initial mycroft-files with custom files, that are needed for the survey functionality.

    
## mycroft_skill.py
### new methods:
#### ask_and_save(survey, number, utterance, timestamp)
* ``survey``: list which saves content to be saved at the end
* ``number``: question number which should be asked
* ``utterance``: skill context
* ``timestamp``: to name the audio files of the user "uniformly"

This method is responsible for interaction with the internal dialog-handler (listener.py).
It uses ``get_question()`` to pick a question and asks it to the user. After the user gave his answer, it renames the audio-file that contains - s.t. the file name contains a timestamp and a question identifier.
In addition it appends ``utterance``, the asked question and the given answer to ``survey``.


#### skill_interaction_response(utterance)
* ``utterance``: context, which skill triggers survey

Entry point for survey. This is the method that has to be inserted in participating skills and is called by them. 
It manages asking questions and saving user responses by calling ``ask_and_save()`` and writes the contents of the user interaction with the survey into a JSON file. 

The JSON contains:
* context (e.g. the skill the user interacted with)
* asked question
* given answer

Example:
```
[
    [
        "joke skill",
        "Did you know you lost private information?",
        "yes"
    ]
]
```

#### get_question(number) 
* ``number``: identifier of question which should be asked

This method provides a dictionary with questions and returns them based on the identifier it is called with.


### adjusted existing methods:
#### init_dialog()
Adjusted s.t. in every case there will be a DialogLoader created, even if the skill doesnt need one. Because the DialogLoader is needed to perform the user survey.

#### __get_response()
Adjusted ``event.wait(15)`` to ``event.wait(25)`` s.t. the time the skill waits until a response is expected is increased. This is necessary to enable processing longer user answers.
> The wait value should be ~10 more than mic.py's x in ``RECORDING_TIMEOUT = x``
## listener.py
### adjusted existing methods:
#### run()
```                        
with open('audio_file_user.wav', 'wb') as f:
    f.write(audio.get_wav_data())
```
Adjusted s.t. the listener perceives noise/speech it records it and saves the recording as a .wav file. Whenever audio is perceived, the listener overwrites the preceding recording. 
Permanent saving of the audio recording is handled by ``ask_and_save()`` in mycroft_skill.py and happens only in skills that are part of the user study.

## mic.py
### adjusted constants:

``MIN_SILENCE_AT_END = 0.75`` increased from ``.25`` s.t. the user has more time of silence until mycroft considers a phrase complete.

``RECORDING_TIMEOUT = 15.0`` increased from ``10.0`` to allow 15 seconds of user response recording.
> RECORDING_TIMEOUT should be ~10 less than mycroft_skill.py's x in ``event.wait(x)``

# Run the Example


# Credits
#### mycroft.ai: 
Devs behind mycroft (https://github.com/mycroftai and https://mycroft.ai/). 



