import sqlite3
from logger import Logger
from servant import Servant

class Scheduler():
    def __init__(self):
        self.logger = Logger()
        self.servant = Servant()
    
    def test(self):
        matches = self.servant.get_history()
        for row in matches:
            pass

        min_id, max_id = min(x['match_id'] for x in matches), max(x['match_id'] for x in matches)
        print(min_id, max_id, max_id-min_id)

        match = self.servant.get_match(5425617019)


if __name__ == '__main__':
    scheduler = Scheduler() 
    scheduler.test()
