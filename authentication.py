import sqlite3

def authenticate(email):
    con = sqlite3.connect("roboadvisor.db")
    cursor = con.cursor()
    cursor.execute("SELECT email FROM user WHERE email='%s'"%email)
    output = cursor.fetchone()
    if output is None:
        # print("No entry")
        cursor.execute("INSERT INTO user(email, status) VALUES ('%s', 0)"%email)
        con.commit()
        # send_otp()
    else:
        # send_otp()
        pass
    con.commit()
    con.close()

def store_predictions(email, equity, mf, debt, cash):
    con = sqlite3.connect("roboadvisor.db")
    cursor = con.cursor()
    cursor.execute("UPDATE user SET status=2, equity=%d, mf=%d, debt=%d, cash=%d WHERE email='%s'"%(equity, mf, debt, cash, email))
    con.commit()
    con.close()

def incomplete(email):
    con = sqlite3.connect("roboadvisor.db")
    cursor = con.cursor()
    cursor.execute("SELECT age,income,duration,risk,plan,gender FROM user WHERE email='%s'"%email)
    output = cursor.fetchone()
    # print(output)
    con.commit()
    if output is None or None in output:
        cursor.execute("UPDATE user SET status=1 WHERE email='%s'"%email)
        con.commit()
        con.close()
        return output,True
    con.close()
    return output,False


authenticate("shashankbudem@gmail.com")
arr,status = incomplete("shashankbudem@gmail.com")
