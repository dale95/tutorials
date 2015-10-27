import urllib2 

req = urllib2.Request('http://www.facebook.com')

try: urllib2.urlopen(req)

except urllib2.URLError as e:

	print e.reason

else:

	print 'site is up'

	code = urllib2.urlopen(req).getcode()


if code == 200:

	print '200 - OK'

elif code == 404:

	print 'Not found'

elif code == 500

	print 'error'

else:

	print 'No code'

