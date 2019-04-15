import mysql.connector

conn = mysql.connector.connect(user='root', password='password', database='wechat_database')
cursor = conn.cursor()
cursor.execute('select * from account_tables')
value = cursor.fetchall()
print(value)