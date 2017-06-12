#! /usr/bin/env python
#Title: detect.py
#Author: Kyna Mowat-Gosnell
#Date: 9/6/17

import qi
import sys
import time
import argparse

class faceDetection(object):

	def __init__(self, app):
		""" initialising qi and face detect event detection """
		super(faceDetection, self).__init__() #super(type, [object or type]). super returns a proxy object that delegates method calls to a parent or sibling class of 'type'
		app.start()
		session = app.session
		#Get the services ALMemory, ALTextToSpeech, and ALFaceDetection
		self.memory = session.service("ALMemory")
		self.tts = session.service("ALTextToSpeech")
		self.detect_faces = session.service("ALFaceDetection")

		#Subscribe to event callback
		self.subscriber = self.memory.subscriber("FaceDetected")
		self.subscriber.signal.connect(self.human_detected)
		self.detect_faces.subscribe("faceDetection")

		self.got_face = False

	def human_detected(self, value):
		# callback for event FaceDetected"""
		if value == []: #value is empty when no face detected
			self.got_face = False
		elif not self.got_face:
			self.got_face = True
			print "Holy Moly, I have seen a face outside of my virtual reality"
			self.tts.say("Hello, human!")

			#First Field = TimeStamp
			timeStamp = value[0]
			print "Time stamp:	" + str(timeStamp)

			#Second Field = array of face information

			faceInfoArray = value[1]
			for j in range(len(faceInfoArray) - 1):
				faceInfo = faceInfoArray[j]

				#First field = face shape information
				faceShapeInfo = faceInfo[0]

				#Second Field = other information
				faceOtherInfo = faceInfo[1]

				print "Face Information:	alpha %.3f - beta %.3f" % (faceShapeInfo[1], faceShapeInfo[2])
				print "Face Information:	width %.3f - height %.3f" % (faceShapeInfo[3], faceShapeInfo[4])
                print "Other Face Info :	" + str(faceOtherInfo)

	def run(self):
  		#Loop created, wait for event trigger until manual interuption
  		print "Starting Face Detection"
    	try:
    		while True:
    			time.sleep(1)
    	
    	except KeyboardInterrupt:
    			print "Interrupted by user, stopping Face Detection"
    			self.detect_faces.unsubscribe("faceDetection")
    			sys.exit(0)
   	if __name__ == "__main__":
   		parser = argeparse.ArgumentParser()
   		parser.add_argument("--ip", type=str, default="pepper.local", help="Pepper IP address. On Pepper or Local Naoqi: use '192.168.1.8")
    	parser.add_argument("--port", type=int, default=9559, help="NAOqi port number")

    	args = parser.parse_args()
    	try:
    		#initialise qi
    		connection_url = connection_url = "tcp://" + args.ip + ":" + str(args.port)
    		app = qi.Application(["faceDetection", "--qi-url=" + connection_url])
    	except RuntimeError:
    		print "Runtime Error"
    		sys.exit(1)

    	face_detection = faceDetection(app)
    	face_detection.run()




