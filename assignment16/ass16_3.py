#Q.3- Update any values in any of the tables. Print the original and updated values.

import pymysql as py

db=py.connect("localhost","root","root","acadview")
cursor=db.cursor()
cursor.execute("select * from book")
print(cursor.fetchall())

try:
	cursor.execute("update book set book_id=420 where name='abc'")
	db.commit()
except:
	db.rollback()
	
cursor.execute("select * from book")
print(cursor.fetchall())
db.close()

