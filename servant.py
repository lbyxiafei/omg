import sqlite3
from logger import Logger

class Servant():
    def __init__(self):
        self.logger = Logger()

    def get():
        pass

    def get_key(self):
        return self.get_keys()[0]

    def get_keys(self):
        con = sqlite3.connect(r"D:\\OMG\\OMG.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM Coffer")
        keys = []
        for row in cur.fetchall():
            keys.append(row[1])
        con.close()
        return keys 
