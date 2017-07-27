from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice
import time
# 1120 golds
times = 20

device=MonkeyRunner.waitForConnection()  

#main-->adventrue
print 'main-->adventrue'
device.touch(1650,800,'DOWN_AND_UP')
time.sleep(2)

#task
print 'task'
device.touch(960,500,'DOWN_AND_UP')
time.sleep(3)

#next
print 'next'
device.touch(1670,985,'DOWN_AND_UP')
time.sleep(3)

while times>0:
	#start challenge
	print 'start challenge'
	device.touch(1460,938,'DOWN_AND_UP')
	time.sleep(24)
	#jump
	print 'jump'
	device.touch(1880,150,'DOWN_AND_UP')
	time.sleep(2)

	#auto
	print 'auto'
	device.touch(1795,44,'DOWN_AND_UP')
	time.sleep(200)
	#click continue
	print 'continue'
	device.touch(960,500,'DOWN_AND_UP')
	time.sleep(3)

	#again
	print 'again'
	device.touch(1460,990,'DOWN_AND_UP')
	time.sleep(5)
	times = times-1


