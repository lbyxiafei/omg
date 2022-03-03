import sqlite3

class Logger():
    def __init__(self, db_file=r"D:\\OMG\\OMG.db", db_table="Logger"):
        self.db=db_file
        self.table=db_table

        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.table}(
                ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                Level INT,
                Message VARCHAR(64),
                Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
            )
        ''')
        con.commit
        con.close()
    
    def log(self, record):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute(f"INSERT INTO {self.table} (Level, Message) VALUES (?,?)",record) 
        con.commit()
        con.close()
    
    def debug(self, m):
        self.log((0, m))

    def info(self, m):
        self.log((1, m))

    def warning(self, m):
        self.log((2, m))

    def error(self, m):
        self.log((3, m))

    def critical(self, m):
        self.log((4, m))

