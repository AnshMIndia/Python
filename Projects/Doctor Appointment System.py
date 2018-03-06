import mysql.connector as MySQL
Connection = MySQL.connect(host="localhost",user="root",passwd= "root",db="mysql")
Cursor = Connection.cursor()
Cursor.execute("""CREATE DATABASE IF NOT EXISTS DoctorsAppointmentSystem;""")
Cursor.execute("""USE DoctorsAppointmentSystem;""")
Cursor.execute("""CREATE TABLE IF NOT EXISTS ADMIN(FIRST_NAME CHAR(20), LAST_NAME CHAR(20), AGE INT, SEX CHAR(1),USERNAME VARCHAR(20), PASSWORD VARCHAR(20));""")
Cursor.execute("""CREATE TABLE IF NOT EXISTS DOCTORS(id INT NOT NULL AUTO_INCREMENT,FIRST_NAME CHAR(20), LAST_NAME CHAR(20), AGE INT, SEX CHAR(1), PRIMARY KEY (id));""")
Cursor.execute("""CREATE TABLE IF NOT EXISTS APPOINTMENTS(id INT NOT NULL AUTO_INCREMENT,FIRST_NAME CHAR(20), LAST_NAME CHAR(20), AGE INT, SEX CHAR(1), PRIMARY KEY (id));""")
Cursor.execute("""CREATE TABLE IF NOT EXISTS PATIENTS(id INT NOT NULL AUTO_INCREMENT,FIRST_NAME CHAR(20), LAST_NAME CHAR(20), AGE INT, SEX CHAR(1), PRIMARY KEY (id));""")
Cursor.execute("""CREATE TABLE IF NOT EXISTS SYSTEMUSERS(id INT NOT NULL AUTO_INCREMENT,FIRST_NAME CHAR(20), LAST_NAME CHAR(20), AGE INT, SEX CHAR(1), PRIMARY KEY (id));""")
Cursor.execute("CREATE USER IF NOT EXISTS 'ADMIN'@'LOCALHOST';")
class Features():
    def __init__(self,attribute=""):
        self.attribute = attribute
        self.Functions()
    def listing(self):
        Cursor.execute("SELECT * FROM {0};".format(self.attribute))
        Results = Cursor.fetchall()
        for Row in Results:
            ID = Row[0]
            FName = Row[1]
            LName = Row[2]
            print("""ID = {0}, First Name = {1}, Last Name = {2}""".format(ID,FName,LName))
    def Functions(self):
        print(("\n1. Adding New {0}\n2. Edit the Existing {0}\n3. View Details of the {0}\n4. Listing of all {0}".format(self.attribute)),end="\n\n")
        Choice=int(input("Enter Your Choice : "))
        print()
        if (Choice == 1):
            FName = input("Enter your First Name : ")
            LName = input("Enter your Last Name : ")
            Age = int(input("Enter your Age : "))
            Sex = input("Enter your Gender (M/F): ")
            Cursor.execute("""INSERT INTO {4}(FIRST_NAME,LAST_NAME,AGE,SEX) VALUES("{0}","{1}",{2},"{3}");""".format(FName,LName,Age,Sex,self.attribute))
            Connection.commit()
            print("Successfully Added")
        elif (Choice == 2):
            self.listing()
            ID = input("Enter your Serial No. : ")
            FName = input("Enter your First Name : ")
            LName = input("Enter your Last Name : ")
            Age = int(input("Enter your Age : "))
            Sex = input("Enter your Gender (M/F): ")
            Cursor.execute("""UPDATE {5} SET FIRST_NAME='{0}',LAST_NAME='{1}',AGE={2},SEX='{3}' WHERE id = {4}""".format(FName,LName,Age,Sex,ID,self.attribute))
            Connection.commit()
            print("Successfully Updated")
        elif (Choice == 3):
            Cursor.execute("SELECT * FROM {0};".format(self.attribute))
            Results = Cursor.fetchall()
            for Row in Results:
                ID = Row[0]
                FName = Row[1]
                LName = Row[2]
                Age = Row[3]
                Sex = Row[4]
                print("""ID = {4}, First Name = {0}, Last Name = {1}, Age = {2}, Gender = {3}""".format(FName,LName,Age,Sex,ID))
            print()
        elif (Choice == 4):
            self.listing()
            print()
        else:
            print("Invalid Choice")
while(1):
    print("\n1. Manage Appointments\n2. Manage Doctors\n3. Manage Patients\n4. Manage System Users\n5. View Reports\n6. Exit")
    Choice=int(input("Enter Your Choice : "))
    if (Choice == 1):
        Server = Features("Appointments")
    elif (Choice == 2):
        Server = Features("Doctors")
    elif (Choice == 3):
        Server = Features("Patients")
    elif (Choice == 4):
        Server = Features("SystemUsers")
    elif (Choice == 5):
        Attribute = int(input("\n1.Appointments\n2.Doctors\n3.Patients\n4.System Users\nSelect your choice : "))
        if (Attribute == 1): Attribute1 = "Appointments"
        elif (Attribute == 2): Attribute1 = "Doctors"
        elif (Attribute == 3): Attribute1 = "Patients"
        elif (Attribute == 4): Attribute1 = "SystemUsers"
        Cursor.execute("SELECT * FROM {0};".format(Attribute1))
        Results = Cursor.fetchall()
        for Row in Results:
            ID = Row[0]
            FName = Row[1]
            LName = Row[2]
            Age = Row[3]
            Sex = Row[4]
            print("""ID = {4}, First Name = {0}, Last Name = {1}, Age = {2}, Gender = {3}""".format(FName,LName,Age,Sex,ID))
    elif (Choice == 6):
        break
    else:
        print("Invalid Choice")
Connection.commit()
Cursor.close()
Connection.close()
