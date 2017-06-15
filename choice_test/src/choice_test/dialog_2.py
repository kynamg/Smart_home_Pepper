#! /usr/bin/env python
#Title: dialog.py
#Author: Kyna Mowat-Gosnell
#Date: 13/6/17
#Version: 2.0

import qi
import argparse
import sys

if __name__=="__main__":
	from naoqi import ALProxy
	#Get ALDialog service
	test = ALProxy("ALDialog", "pepper.local", 9559)

	#qichat code as strings - end of line characters are important
	topic_content = ('topic: ~cup_of_tea()\n'
					'language: enu\n'
					'concept:(choice) [yes no "yes please" "no thank you"]\n'
					'u: (What ["is the message" "is it"]) Your friend, Mauro, has put the kettle on for a cup of tea. Would you like to do the same, and talk to her over video chat?\n'
						'u1: (yes "yes please") Im sure she is looking forward to it\n'
						'u1: (no "no thank you") are you sure?\n'
							'u2: (yes) okay\n'
							'u2: (no) Im sure she is looking forward to it\n')

	topic_name = test.loadTopicContent(topic_content)
	test.activateTopic(topic_name)
	test.subscribe('tea_dialog')

	try:
		raw_input("\nSpeak to the robot. Press Enter when finished:")
	finally:
		test.unsubscribe('tea_dialog')
        test.deactivateTopic(topic_name)
        test.unloadTopic(topic_name)