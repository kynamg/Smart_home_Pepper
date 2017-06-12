#! /usr/bin/env python
#Title: animate.py
#Author: Kyna Mowat-Gosnell
#Date: 9/6/17

if __name__=="__main__":
	from naoqi import ALProxy

	an_tag = ALProxy("ALAnimatedSpeech", "pepper.local", 9559)
	motion = ALProxy("ALMotion", "pepper.local", 9559)
	
	an_tag.say("^startTag(body language) Hi, I am going to explain how a plumbus is made. First they take the dinglebop, and they smooth it out with a bunch of schleem. The schleem is then repurposed for later batches. They take the dinglebop and push it through the krumbo, where the fleeb is rubbed against it. It's important that the fleeb is rubbed, because the fleeb has all of the fleeb juice. Then a schlomi shows up, and rubs it, and spits on it. They cut the fleeb. There are several hizzards in the way. The blamphs rub against the trumbles, and the plumb-bus and grumbo are shaved away. That leaves you with a regular old plumbus.")
	motion.moveTo(-0.5,0,3.1415)