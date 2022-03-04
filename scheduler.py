import sqlite3
from logger import Logger
from servant import Servant

class Scheduler():
    def __init__(self):
        self.logger = Logger()
        self.servant = Servant()
    
    def test(self):
        matches = self.servant.get_history()
        min_id, max_id = min(x['match_id'] for x in matches), max(x['match_id'] for x in matches)
        p_matches = self.servant.query_pool(min_id, max_id)
        print(len(p_matches))

if __name__ == '__main__':
    scheduler = Scheduler() 
    scheduler.test()
