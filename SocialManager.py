import Logger

class SocialManager(object):
    """Manages friends"""

    def __init__(self,io):
        self.twitterio = io

    def work(self):
        self.addfollowersasfriends()
        
    def addfollowersasfriends(self):
        friends = self.twitterio.getFriends()
        followers = self.twitterio.getFollowers()
        tobeadded = followers[:]
        for follower in tobeadded:
            for friend in friends:
                if friend.screen_name == follower.screen_name:
                    tobeadded = tobeadded.remove(follower)

        for follower in tobeadded:
            self.twitterio.addFriend(follower)


            

