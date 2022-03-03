import sqlite3
from logger import Logger

class Scheduler():
    def __init__(self):
        self.logger = Logger()
    
    def download(self, match_id):
        pass

    def get_key(self):
        con = sqlite3.connect(r"D:\\OMG\\OMG.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM Coffer")
        key = cur.fetchone()[1]
        con.close()
        return key 


if __name__ == '__main__':
    scheduler = Scheduler() 
    scheduler.logger.info("hello world")
    print(scheduler.get_key())
