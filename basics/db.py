import sqlite3
con = sqlite3.connect("Students.db")

cur = con.cursor()

# cur.execute("CREATE TABLE Students (name TEXT,id INTEGER,address STRING, mobile INTEGER, blood group STRING)")

cur.execute("INSERT INTO Students VALUES ('Ruhi','45', 'Basabo', '017536387', 'k+')")

res = cur.execute("SELECT * FROM Students")

print(res.fetchall())