import datetime
import time
import os

print 'starting'

while True:
	fh = open("mytimelog.txt", "a")
	fh.write(str(datetime.datetime.now()) + "\n")
	fh.write(str(os.getloadavg()) + "\n")
	fh.close()

	time.sleep(10)
 

	fh = open("mytimelog.txt", "a")
	fh.write(str(datetime.datetime.now()) + "\n")
	fh.write(str(os.getloadavg()) + "\n")
	fh.close()

	print "done"