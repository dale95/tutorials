import feedparser
feeddata = feedparser.parse('http://www.reddit.com/r/python/.rss')
print feeddata['feed']['title']
print feeddata['entries'][0]['title']

for post(0,5) in feeddata.entries:
	print post.title + ": " + post.link + "\n"
