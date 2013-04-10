import twitter
import Logger

class tweetio(object):
    """Handles all Twitter IO"""

    def __init__(self):

       self.mentions = None
       
       self.latestMentionId = None

       self.latestDirectMessage = None

       self.api = twitter.Api(consumer_key='',
                          consumer_secret='',
                          access_token_key='',
                          access_token_secret='')

       Logger.log(str(self.api.VerifyCredentials()))
 
    def getTimeline(self):
        statuses = self.api.GetUserTimeline()
        Logger.log([s.text for s in statuses])

    def postTweet(self,status):
        tweet = self.api.PostUpdates(status)
        return tweet

    def getFriends(self):
        users = self.api.GetFriends()
        Logger.log([u.name for u in users])
        return users
    
    def getFollowers(self):
        users = self.api.GetFollowers()
        #Logger.log("Followers : " + [u.name for u in users] )
        return users

    def getMentions(self):
        mentions = self.api.GetMentions(since_id=self.latestMentionId)
        if len(mentions) > 0:
            self.latestMentionId = mentions[0].id
            Logger.log([m.id for m in mentions])
            return mentions
        else:
            return None
    
    def getDirectMessages(self):
        dms = self.api.GetDirectMessages(since_id=self.latestDirectMessage)
        if len(dms) > 0:
            self.latestDirectMessage = dms[0].id
            Logger.log([dm.id for dm in dms])
            return dms
        else:
            return None
    
    def addFriend(self,user):
        self.api.CreateFriendship(user.id)
        Logger.log("Added new friend: " + user.screen_name)
        print ("Added new friend: " + user.screen_name)





