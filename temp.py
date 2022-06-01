import sqlite3

con = sqlite3.connect("roboadvisor.db")
print("Database opened successfully")
cursor = con.cursor()
# cursor.execute("create table user (email VARCHAR(225) NOT NULL, status INT NOT NULL, equity INT, mf INT, debt INT, cash INT)")
# print("Table created successfully")
# cursor.execute("INSERT INTO user(email, status) VALUES ('shashank4305@gmail.com', 0)")
# print("Executed successfully")
cursor.execute("SELECT * FROM user")
con.commit()
output = cursor.fetchall()
for row in output:
  print(row)

con.close()