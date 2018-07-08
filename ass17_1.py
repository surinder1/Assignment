# Q.1- Create a database. Create the following tables:
# 1. Book
# 2. Titles
# 3. Publishers
# 4. Zipcodes
# 5. AuthorsTitles
# 6. Authors

import pymysql as py

db=py.connect("localhost","root","root","acadview")
cursor=db.cursor()
cd="create table book(name char(20),book_id int(20),tilte varchar(20),genre int(20))"
cursor.execute(cd)
cd="create table title(title_id int(20),title name(20),isbn int(20),publisher_id int(20),publisation_year int(5))"
cursor.execute(cd)
cd="create table publishers(piblisher_id int(20),name char(20),address char(20),suite_no int(20),zip_code int(20))"
cursor.execute(cd)
cd="create table zipcodes(zip_code int(20),city cahr(20),state char(20),zip_code int(20))"
cursor.execute(cd)
cd="create table author(name char(20),auther_id int(20),tilte_id int(20))"
cursor.execute(cd)

db.close()

