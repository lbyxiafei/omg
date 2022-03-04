import requests
import sqlite3
from logger import Logger

class Servant():
    def __init__(self, db_file=r"D:\\OMG\\OMG.db"):
        self.db=db_file
        self.logger = Logger()
        self.keys = []
        self.get_keys()

    def get_match(self, match_id):
        url = f"https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v001/?match_id={match_id}&key={self.keys[0]}"
        response = requests.get(url)
        data = response.json()
        return data['result']

    def get_history(self):
        url = f"https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key={self.keys[0]}"
        response = requests.get(url)
        data = response.json()
        return data['result']['matches']
    
    def query_pool(self, min_id, max_id):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute(f"SELECT * from Pool WHERE MatchID>={min_id} AND MatchID<={max_id}")
        matches = []
        for row in cur.fetchall():
            matches.append(row)
        return matches

    def upsert_pool(self):
        pass

    def get_key(self):
        if len(self.keys)>0:
            return self.keys[0]
        return self.get_keys()[0]

    def get_keys(self):
        if len(self.keys)>0:
            return self.keys
        con = sqlite3.connect(r"D:\\OMG\\OMG.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM Coffer")
        for row in cur.fetchall():
            self.keys.append(row[1])
        con.close()
        self.logger.info(f"Retrieve keys: {self.keys} from omg.logger.")
        return self.keys
