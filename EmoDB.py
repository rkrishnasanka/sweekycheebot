import sqlite3

class QuotesContext(object):
    """Handles all EmoDB"""
    
    def __init__(self):

        self.conn = sqlite3.connect("emobase.db")
        self.cursor = self.conn.cursor()
 
    def getRandomQuote(self):
        self.cursor.execute("""SELECT quote FROM quotes ORDER BY RANDOM() LIMIT 1; """)
        return (self.cursor.fetchone())[0]
    
    def insertQuote(self,quote):
        self.cursor.execute("INSERT INTO quotes VALUES (?)",[quote])
        self.conn.commit()


