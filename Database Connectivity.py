import mysql.connector as MySQL
User1 = input("Enter your username:")
Passwd1 = input("Enter your password;")
DB1 = input("Enter you Database Name:")
Connection = MySQL.connect(host="localhost",user=User1,passwd= Passwd1,db=DB1)
Cursor = Connection.cursor()
Cursor.execute("SELECT VERSION()")
Data = Cursor.fetchone()
print ( "Database Version : %s " %Data,end="\n\n")
Cursor.execute("""CREATE TABLE IF NOT EXISTS DATABASE_1(id MEDIUMINT NOT NULL AUTO_INCREMENT,FIRST_NAME CHAR(20), LAST_NAME CHAR(20), AGE INT, SEX CHAR(1), PRIMARY KEY (id));""")
j = 0
Cursor.execute("SELECT COUNT(*) FROM DATABASE_1;")
actualID = (Cursor.fetchall()[0][0])
while j == 0:
    Cursor.execute("SELECT COUNT(*) FROM DATABASE_1;")
    actualID = (Cursor.fetchall()[0][0])+1
    print("1. Insert\n2. Read\n3. Update\n4. Delete",end="\n\n")
    Choice=int(input("Enter Your Choice : "))
    if (Choice == 1):
        FName = input("Enter your First Name : ")
        LName = input("Enter your Last Name : ")
        Age = int(input("Enter your Age : "))
        Sex = input("Enter your Gender (M/F): ")
        String = """INSERT INTO DATABASE_1 VALUES({4},"{0}","{1}",{2},"{3}");""".format(FName,LName,Age,Sex,actualID)
        Cursor.execute(String)
        Connection.commit()
        print("Successfully Inserted")
        NChoice = input("Do you want to choose different choice (Y/N) : ")
        print()
        if (str.upper(NChoice)=="N"): j=1
    elif (Choice == 2):
        Cursor.execute("SELECT * FROM DATABASE_1;")
        Results = Cursor.fetchall()
        for Row in Results:
            ID = Row[0]
            FName = Row[1]
            LName = Row[2]
            Age = Row[3]
            Sex = Row[4]
            print("""ID = {4}, First Name = {0}, Last Name = {1}, Age = {2}, Gender = {3}""".format(FName,LName,Age,Sex,ID))
        NChoice = input("Do you want to choose different choice (Y/N) : ")
        Connection.commit()
        print()
        if (str.upper(NChoice)=="N"): j=1
    elif (Choice == 3):
        ID = input("Enter your Serial No. : ")
        FName = input("Enter your First Name : ")
        LName = input("Enter your Last Name : ")
        Age = int(input("Enter your Age : "))
        Sex = input("Enter your Gender (M/F): ")
        String = ("""UPDATE DATABASE_1 SET FIRST_NAME='{0}',LAST_NAME='{1}',AGE={2},SEX='{3}' WHERE id = {4}""".format(FName,LName,Age,Sex,ID))
        Cursor.execute(String)
        Connection.commit()
        print("Successfully Updated")
        NChoice = input("Do you want to choose different choice (Y/N) : ")
        if (str.upper(NChoice)=="N"): j=1
        print()
    elif (Choice == 4):
        ID = input("Enter your Serial No. : ")
        String = ("""DELETE FROM DATABASE_1 WHERE id = {0}""".format(ID))
        Cursor.execute(String)
        Connection.commit()
        print("Successfully Deleted")
        NChoice = input("Do you want to choose different choice (Y/N) : ")
        if (str.upper(NChoice)=="N"): j=1
        print()
    else:
        print("Invalid Choice")
Satisfaction = input("Are you satisfied with you changes (Y/N) : ")
if (str.upper(Satisfaction) == "N"):
    Connection.rollback()
Cursor.close()
Connection.close()
