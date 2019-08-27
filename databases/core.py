import pymysql

global connection, cursor
try:
    connection = pymysql.connect(host='localhost', port=3306, db='classicmodels', user='root', passwd='root')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM classicmodels.products limit 10")
    record = cursor.fetchall()
    # print("Your result : ", record)
    for s in record:
        print(s)
except Exception as e:
    print("Error while connecting to MySQL", e)
finally:
    cursor.close()
    connection.close()
    print("MySQL connection is closed")
