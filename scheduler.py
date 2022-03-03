import sqlite3
from logger import Logger
from servant import Servant

class Scheduler():
    def __init__(self):
        self.logger = Logger()
        self.servant = Servant()
    
    def download(self, match_id):
        pass

if __name__ == '__main__':
    scheduler = Scheduler() 
    key = scheduler.servant.get_key()
    print(key)
    keys = scheduler.servant.get_keys()
    print(keys)
