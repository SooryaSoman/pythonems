import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='soorya123#',
    database='ems'
)
cursor=mydb.cursor()
cursor.execute("select* from employee")
rows=cursor.fetchall()
for row in rows:
    print(row)
    cursor.close()
    mydb.close()