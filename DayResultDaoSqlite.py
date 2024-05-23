import sqlite3

from DayResultDao import DayResultDao

class DayResultDaoSqlite(DayResultDao) :
    def __init__(self) :
        self.conn = None

    def create_connection(self, url ):
        try:
            self.conn = sqlite3.connect(url)
        except sqlite3.Error as e:
            print(e)
        return self.conn

    def create_data( self, values ):
        sql = '''INSERT INTO CA(date,ca,hours,hsup,comment) VALUES (?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, values)
        self.conn.commit()
        return cur.lastrowid

    def update_data( self, values) :
        sql = '''UPDATE CA SET date=? , ca=?, hours=?, hsup=?, comment=? WHERE date= ? '''
        cur = self.conn.cursor()
        cur.execute(sql, values)
        self.conn.commit()

    def read_data( self, day) :
        sql = '''SELECT * FROM CA WHERE date=?'''
        cur = self.conn.cursor()
        res = cur.execute(sql, (day,) )
        return res.fetchone()

    def destroy_data( self, day ) :
        sql = '''DELETE FROM CA WHERE date=?'''
        cur = self.conn.cursor()
        cur.execute(sql, (day,) )
        self.conn.commit()

    def read_all_data( self ) :
        sql = '''SELECT date FROM CA ORDER BY date ASC'''
        cur = self.conn.cursor()
        res = cur.execute(sql)
        return res

    def close(self) :
        self.conn.close()
