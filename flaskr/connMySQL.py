import MySQLdb
import sys

def connMySQL():
    try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='123123', db='flaskr')
    except Exception, e:
        print e
        sys.exit()
    return conn

if __name__ == '__main__':
    
    cursor = connMySQL().cursor()
    sql = "select * from entries limit 10"
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        print type(data)
        print data
    except Exception, e:
        print e
        sys.exit()



