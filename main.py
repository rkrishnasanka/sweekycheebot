import time
import sys
import twitter 
import EmoDB
import TwitterRemote
import tweetio
import urllib2
import SocialManager

def internet_on():
    try:
        response=urllib2.urlopen('http://74.125.113.99',timeout=1)
        return True
    except urllib2.URLError as err: print "No Internet Connection"
    return False

if __name__ == "__main__":
    """Main Loop"""

    io = tweetio.tweetio()
    quotestablecontext = EmoDB.QuotesContext()
    twitterremote = TwitterRemote.TwitterRemote(io)
    #socialworker = SocialManager.SocialManager(io)

    while 1:
        #io.getFriends()
        #io.getTimeline()
        #io.checktweets()
        #io.getMentions()
        #quote = quotestablecontext.getRandomQuote()
        #io.postTweet(quote)
        #time.sleep(60*60*6)
        #if internet_on():
        twitterremote.work()
        #socialworker.work()

        time.sleep(2)
