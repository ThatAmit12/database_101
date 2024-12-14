import sqlite3
con = sqlite3.connect("Students.db")
cur = con.cursor()
cur.execute("CREATE TABLE Students(ID, Name, Address, Mobile, Blood Group)")
res = cur.execute("SELECT * FROM Students")
res.fetchall()