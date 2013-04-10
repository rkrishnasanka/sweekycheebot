import twitter
import re
import Logger
import time
import EmoDB

class TwitterRemote(object):
    """ Twitter Remote control """
    
    def __init__(self,io):
        self.twitterio = io
        self.admins = ['','']#add file read capability here / config file read capability
        self.quotestablecontext = EmoDB.QuotesContext()

    def isadmin(self,twitter_handle):
        """Checks if the user is an admin"""
        if any(twitter_handle in admin for admin in self.admins):
            return True
        return False

    def processAdminCommands(self,commands):
        print commands
        for command in commands :
            if command == "live":
                pass

            if command == "die":
                pass

            if command == "yap":
                quote = self.quotestablecontext.getRandomQuote()
                self.twitterio.postTweet(quote)

            if command == "yawn":
                pass

    def processGeneralCommands(self,commands,directmessage):
        print commands
        for command in commands :
            if command == "unfollow":
                pass


    def parseGeneralDMCommand(self,directmessage):
        
        if time.time() - directmessage.created_at_in_seconds > 60:
            return

        #find all hashtags
        text = directmessage.text
        hts = re.findall(r"#(\w+)", text)

        #checking if the cmd hashtag is present to identify as a command
        self.processGeneralCommands(hts,directmessage)

    def parseAdminDMCommand(self,directmessage):
        
        #checking for time out condition 60s 
        if time.time() - directmessage.created_at_in_seconds > 60:
            return

        #find all hashtags
        text = directmessage.text
        hts = re.findall(r"#(\w+)", text)

        #checking if the cmd hashtag is present to identify as a command
        if any("cmd" in ht for ht in hts):
            Logger.log("Command found: " + directmessage.text)
            hts.remove("cmd")
            self.processAdminCommands(hts)

    def work(self):
        """ Get the mentions , check for commands """
        dms = self.twitterio.getDirectMessages()
        #Check if mentions are empty , if empty return

        if(dms == None):
            return

        for dm in dms:
            #Check if me or sweeky send the mentions
            if self.isadmin(dm.sender_screen_name):
                self.parseAdminDMCommand(dm)
            else:
                self.parseGeneralDMCommand(dm)

        
