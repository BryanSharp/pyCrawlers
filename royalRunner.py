# coding=utf-8
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice
import time
# 1120 golds
times = 20

device=MonkeyRunner.waitForConnection()  



while times>0:
	#main-->adventrue
	print 'main-->adventrue'
	device.touch(1650,800,'DOWN_AND_UP')
	time.sleep(2)

	#task
	print 'task'
	device.touch(960,500,'DOWN_AND_UP')
	time.sleep(2)

	#next
	print 'next'
	device.touch(1670,985,'DOWN_AND_UP')
	time.sleep(2)
	#start challenge
	print 'start challenge'
	device.touch(1460,938,'DOWN_AND_UP')
	time.sleep(20)
	#jump
	print 'jump'
	device.touch(1880,150,'DOWN_AND_UP')
	time.sleep(1)

	#auto
	print 'auto'
	device.touch(1795,44,'DOWN_AND_UP')
	time.sleep(195)
	#click continue
	print 'continue'
	device.touch(960,500,'DOWN_AND_UP')
	time.sleep(2)

	#again
	print 'again'
	device.touch(1460,990,'DOWN_AND_UP')
	time.sleep(2)

	#back
	print 'back1'
	device.touch(1150,990,'DOWN_AND_UP')
	time.sleep(2)

	#back
	print 'back2'
	device.touch(100,70,'DOWN_AND_UP')
	time.sleep(2)

	#back
	print 'back3'
	device.touch(100,70,'DOWN_AND_UP')
	time.sleep(2)

	# Takes a screenshot
	result = device.takeSnapshot()
	# Writes the screenshot to a file
	result.writeToFile('shot%d.png'%times,'png')
	time.sleep(1)

	times = times-1

	



