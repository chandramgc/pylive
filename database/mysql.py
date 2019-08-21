import pymysql


def get_mysql_version():
    global connection, cursor
    try:
        connection = pymysql.connect(host='localhost', port=3306, db='classicmodels', user='root', passwd='root')
        db_info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)
    except Exception as e:
        print("Error while connecting to MySQL", e)
    finally:
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
