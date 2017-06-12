def say(name):
	print('Hello ' + name)

	from naoqi import ALProxy
#	tts = ALProxy("ALTextToSpeech", "pepper.local", 9559)
	motion = ALProxy("ALMotion", "pepper.local", 9559)
	#animatespeech = ALProxy("ALAnimatedSpeech", "pepper.local", 9559)
	#neutral = ALProxy("ALRobotPosture", "pepper.local", 9559)
	motion.wakeUp()
	motion.moveTo(0.5,0.1,0)
	motion.rest()
#	tts.say("Hello, I have a message for you")
#	animatespeech.say("Hello. I am trying to see if i can talk and the action happens during my speech ^start(animations/Stand/Gestures/Explain_1)")
#	neutral.goToPosture("StandInit", 0.5)