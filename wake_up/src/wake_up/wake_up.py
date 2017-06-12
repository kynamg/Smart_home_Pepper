def wake(pepper):

	from naoqi import ALProxy

	motion = ALProxy("ALMotion","pepper.local", 9559)
	motion.wakeUp()