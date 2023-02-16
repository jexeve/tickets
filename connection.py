import pymysql

def connectDB():
    return pymysql.connect(host='localhost',
                        user='root',
                        password='',
                        db='tickets',
                        )