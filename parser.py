import feedparser


# this function only fetches and parses feed through url
def feed_parser(feed):
 feed=feedparser.parse(feed)
 return feed