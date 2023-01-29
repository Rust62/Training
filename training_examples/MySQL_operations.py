import mysql.connector


try:
    con = mysql.connector.connect(host="127.0.0.1", port=3306, user='root',passwd='1999', database='sql_mydb')
    curs = con.cursor()
    curs.execute("SELECT * FROM sql_mydb.test_data")

    for row in curs:
        print(row[0], row[1], row[2], row[3], row[4], row[5])
    con.close()
except:
    print("connection unsuccessful...")
    print("Finished...")
