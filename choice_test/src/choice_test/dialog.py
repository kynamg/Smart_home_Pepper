#! /usr/bin/env python
#Title: dialog.py
#Author: Kyna Mowat-Gosnell
#Date: 13/6/17

import qi
import argparse
import sys

def dialog(session):
	
	#Get ALDialog service
	ALDialog = session.service("ALDialog")
    ALDialog.setLanguage("English")

	#qichat code as strings - end of line characters are important
	topic_content = ('topic: ~cup_of_tea()\n'
					'language: enu\n'
					'concept:(choice) [yes no "yes please" "no thank you"]\n'
					'u: (What ["is the message" "is it"]) Your friend, Michelle, has put the kettle on for a cup of tea. Would you like to do the same, and talk to her over video chat? Your friend, Michelle, has put the kettle on for a cup of tea. Would you like to do the same, and talk to her over video chat?\n'
						'u1: (yes "yes please") Im sure she is looking forward to it\n'
						'u1: (no "no thank you") are you sure?\n'
							'u2: (yes) okay\n'
							'u2: (no) Im sure she is looking forward to it\n')

	topic_name = ALDialog.loadTopicContent(topic_content)
	test.activateTopic(topic_content)
	test.subscribe('tea_dialog')

	 try:
        raw_input("\nSpeak to the robot. Press Enter when finished:")
    finally:
        # stopping the dialog engine
        ALDialog.unsubscribe('tea_dialog')

        # Deactivating all topics
        ALDialog.deactivateTopic(topic_name)

        # now that the dialog engine is stopped and there are no more activated topics,
        # we can unload all topics and free the associated memory
        ALDialog.unloadTopic(topic_name)