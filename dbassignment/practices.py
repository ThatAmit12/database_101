import sqlite3
con = sqlite3.connect("practice.db")
cur = con.cursor()
#cur.execute("CREATE TABLE Students(SID TEXT PRIMARY KEY,Name TEXT, Mobile_number INTEGER)")
cur.execute("INSERT INTO Students values('567','Amit','0358603')")
cur.execute("CREATE TABLE Courses(CID TEXT PRIMARY KEY,Course_Name TEXT,SID TEXT, FOREIGN KEY(SID) REFERENCES Students(SID))")
cur.execute("INSERT INTO Courses values('CSE1201','Compiler Design','567')")
cur.fetchall()
con.commit()
cur.execute("SELECT*FROM Students")
cur.execute("SELECT*FROM Courses")
print(cur.fetchall())


