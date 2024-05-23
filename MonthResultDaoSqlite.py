import sqlite3

from MonthResultDao import MonthResultDao

class MonthResultDaoSqlite(MonthResultDao):
    def __init__(self) :
        self.conn = None

    def create_connection(self, url) :
        try:
            self.conn = sqlite3.connect(url)
        except sqlite3.Error as e:
            print(e)
        return self.conn

    def get_days(self, year, month) :
        sql = '''SELECT date FROM CA WHERE date LIKE ?'''
        cur = self.conn.cursor()
        cur.execute(sql, (f"{year}-{month}-%", ) )
        rows = cur.fetchall()
        days = []
        for r in rows :
            days.append( r[0] )
        return days

    def get_ca(self, year, month) :
        sql = '''SELECT SUM(ca) FROM CA WHERE date LIKE ?'''
        cur = self.conn.cursor()
        res = cur.execute(sql, (f"{year}-{month}-%", ) )
        return res.fetchone()[0]

    def get_hours(self, year, month) :
        sql = '''SELECT SUM(hours) FROM CA WHERE date LIKE ?'''
        cur = self.conn.cursor()
        res = cur.execute(sql, (f"{year}-{month}-%", ) )
        return res.fetchone()[0]

    def get_hsup(self, year, month) :
        sql = '''SELECT SUM(hsup) FROM CA WHERE date LIKE ?'''
        cur = self.conn.cursor()
        res = cur.execute(sql, (f"{year}-{month}-%", ) )
        return res.fetchone()[0]

    def get_prime(self, year, month, seuil) :
        sql = '''SELECT SUM(ca) - ? FROM CA WHERE date LIKE ?'''
        cur = self.conn.cursor()
        res = cur.execute(sql, (seuil, f"{year}-{month}-%", ) )
        return res.fetchone()[0]
