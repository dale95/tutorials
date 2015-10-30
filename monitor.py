import time

print "Hello \n"
print "Waiting 5 seconds \n"

t = 6
while t > 1:
	time.sleep(t)
	t = t-1
	print t

print "Back"