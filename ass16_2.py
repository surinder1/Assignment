#Q.2- Insert values in the tables.

import pymysql as py

db=py.connect("localhost","root","root","acadview")
cursor=db.cursor()

try:
	cursor.execute("insert into book values('abc',120,'def',340)")
	db.commit()
	
except:
	db.rollback()
	
qr="insert into publishers values(324,'abc','def',97,98)"
try:
	cursor.execute(qr)
	db.commit()
except:
	db.rollback()
	
qr="insert into title values(345,'acr',567,340,456)"
try:
	cursor.execute(qr)
	db.commit()
except:
	db.rollback()
	
qr="insert into zip_code values(876,'pqr','def')"
try:
	cursor.execute(qr)
	db.commit()
except:
	db.rollback()

qr="insert into author values('abc',120,340)"
try:
	cursor.execute(qr)
	db.commit()
except:
	db.rollback()
	
db.close()