from postgres_config import dbConfig
import psycopg2 as pyo

con = pyo.connect(**dbConfig)
cursor = con.cursor()

class Politics_db:
    def __init__(self):
        self.con = pyo.connect(**dbConfig)
        self.cursor = con.cursor()
        print("you have connected to the database")
        print(con)


db = Politics_db()