#! /usr/bin/env python
#Title: showImage.py
#Author: Kyna Mowat-Gosnell
#Date: 14/6/17
#Version: 1.0

import qi
import argparse
import sys
import time

if __name__=="__main__":
	from naoqi import ALProxy

	tabletService = ALProxy("ALTabletService", "pepper.local", 9559)
	try:
		#preload image url
		tabletService.preLoadImage("http://198.18.0.1/apps/doxy-4a0f9d/doxy.jpeg")

		tabletService.showImage("http://198.18.0.1/apps/doxy-4a0f9d/doxy.jpeg")

		time.sleep(5)
		tabletService.hideImage()
	
	except Exception, e:
		print "Error was: ", e