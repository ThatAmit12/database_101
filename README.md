# database_101
 data_vandar
## How to create a database table in SQLite
~~~
import sqlite3
con = sqlite3.connect("tutorial.db")


cur = con.cursor()

cur.execute("CREATE TABLE movie(title,year,score)")

res = cur.execute("SELECT * FROM movie")

res.fetchall()
~~~
