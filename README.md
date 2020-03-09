# mycroft-skill-addon
Enhancements for mycroft-skills to conduct user-centric studies.

# Contents
* [About](#about)
* [Setup](#setup)
* [Components](#components)
* [Run the Example](#run-the-example)
* [Credits](#credits)

# About

# Setup
* Setup and pair your device by following the official documentation: ```https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/get-mycroft```
* Installing our skill by executing the following terminal command: ```msm install https://github.com/justfaked/mycroft-skill-addon.git```
* Navigate to ```\mycroft-core\mycroft\skills\mycroft-skill-addon.justfaked\``` and move the included ```start.sh``` script into the ```\mycroft-core\``` folder.
* Execute the script via the command ```$ bash start.sh```
* Modify all skills that shall be included in the user study
* Reboot the device

# Components
* start.sh
    
* mycroft_skill.py
    - new methods:
        - ask_and_save()
        Args: survey: List, number: Int, utterance: String, timestamp: String
        ''' Asks specific question and appends user interaction, in addition it renames and saves the audio files of the user
        :param survey: list which saves content to be saved at the end
        :param number: question number which should be asked
        :param utterance: skill context
        :param timestamp: to name the audio files of the user "uniformly"
        '''
        ```Is responsible for communication with the dialog-handler. Here questions are aksed and answers received. Survey is a collection to store utterance, question and answer for later processing. ```
        - skill_interaction_response()
        Args: utterance: String
        '''Will be called by any skill and manages asking and saving
        :param utterance: context, which skill triggers survey
        '''
        ```Entry point for survey. This is the method that has to be inserted in participating skills. It manages asking qustions and saving user responses. User responses as JSON-files. The JSON contains the utterance (context), the asked question(s) and the users response as text.```
        - get_question() 
        Args: number: Int
        :param number: number of question which should be asked
        :return: question
        ```Represents our questionnaire, returns a number-specific question.```
    - adjustments to existing methods:
        - init_dialog()
         ```In every case there will be a DialogLoader created, even if the skill doesnt need one. Because the DialogLoader is needed to perform the user survey.```
        - __get_response()
        ``` event.wait(25) increased time the skill waits until a response is expected. This is necessary to enable processing longer user answers.```

* listener.py

* mic.py


# Run the Example


# Credits


