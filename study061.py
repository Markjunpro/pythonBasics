import mysql.connector
conn = mysql.connector.connect(user='root',password='lijun',database='test')
cursor = conn.cursor()
cursor.execute('creat table user (id varchar(20) primary key ,name varchar(20))')
cursor.execute('insert into user (id,name) values (%s ,%s)',['1','lijun'])
print(cursor.rowcount)
print('\n')
conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.excute('select * from user where id = %s',('1',))
values = cursor.fetchall()
print(values)
print('\n')
print(cursor.close())
conn.close()

