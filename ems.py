from os import system
import re
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="ems")
mycursor = con.cursor()

regax = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
pattern = re.compile("(0|91)?[7-9][0-9]{9}")


def Add_Employ():
    print("{:>60}".format("-->> Add Emplyee Record <<--"))
    Id = input("Enter Employee Id: ")
    if (check_employee(Id) == True):
        print("Employee ID Already Exists\nTry Again..")
        press = input("Press any key to continue..")
        Add_Employ()
    Name = input("Enter Employee Name: ")
    if (check_employee_name(Name) == True):
        print("Employee Name Already Exists\nTry Again..")
        press = input("Press any key to continue..")
        Add_Employ()
    Emial_Id = input("Enter Employee e-mail: ")
    if (re.fullmatch(regax, Emial_Id)):
        print('Valid Email')
    else:
        print("Invalid Email")
        press = input("Press any key to continue..")
        Add_Employ()
    Phone_no = input("Enter Employee Phone #: ")
    if (pattern.match(Phone_no)):
        print('Valid Phone #')
    else:
        print("Invalid Phone #")
        press = input("Press any key to continue..")
        Add_Employ()    
    Address = input("Enter Employee Address: ")
    Post = input("Enter Employee Post: ")
    Salary = input("Enter Employee Salary: ")
    data = (Id, Name, Emial_Id, Phone_no, Address, Post, Salary)
    sql = 'insert into empdata values(%s,%s,%s,%s,%s,%s,%s)'
    c = con.cursor()

    c.execute(sql, data)
    con.commit()
    print("Successfully Added Employee")
    press = input('Press any key to continue..')
    menu()

def check_employee_name(employee_name):
    sql = 'select * from empdata where Name=%s'   
    c = con.cursor(buffered=True)
    data = (employee_name,)
    c.execute(sql, data)

    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

# Function to Check Employee

def check_employee(employee_id):
    sql = 'select * from empdata where Id=%s'   
    c = con.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql, data)

    r = c.rowcount
    if r == 1:
        return True
    else:
        return False


# Function to Display Employee

def Display_Employ():
    print("{:>60}".format("-->> Add Employee Record <<--"))
    sql ='select * from empdata'
    c = con.cursor()

    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("Employee Id: ", i[0])
        print("Employee Name: ", i[1])
        print("Employee Email: ", i[2])
        print("Employee Phone: ", i[3])
        print("Employee Address: ", i[4])
        print("Employee Post: ", i[5])
        print("Employee Salary: ", i[6])
        print("\n")
        press = input("Press any key to continue..")
        menu()

# Function to Update Employee

def Update_Employ():
    print("{:>60}".format("-->> Update Employee Record <<--"))
    Id = input("Enter Employee Id: ")
    if (check_employee(Id) == False):
        print("Employee ID Doesn't Exists\nTry Again..")
        press = input("Press any key to continue..")
        Update_Employ()
    else:
        Emial_Id = input("Enter Employee e-mail: ")
        Phone_no = input("Enter Employee Phone #: ")
        Address = input("Enter Employee Address: ")
    
    #updating employee details in the empdata table
    sql = 'UPDATE empdata set Emial_Id = %s, Phone_no = %s, Address = %s where Id = %s'
    data = (Emial_Id, Phone_no, Address, Id)
    c = con.cursor()

    #Executing the sql query
    c.execute(sql, data)
    #commit() method to make changes in the table
    con.commit()
    print("Updated Employee Record")
    press = input("Press any key to continue..")
    menu()

#Function to Promote Employee
def Promote_Employ():
    print("{:>60}".format("-->> Promoting Employee <<--"))
    Id = input("Enter Employee Id: ")
    if (check_employee(Id) == False):
        print("Employee ID Doesn't Exists\nTry Again..")
        press = input("Press any key to continue..")
        Promote_Employ()
    else:
        Post = input("Enter Employee Post: ")
        Salary = input("Enter Employee Salary: ")
    sql = 'UPDATE empdata set Post = %s, Salary = %s where Id = %s'
    data = (Post, Salary, Id)
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Successfully Employee Promoted")
    press = input('Press any key to continue..')
    menu()

#Function to Remove Employee
def Remove_Employ():
    print("{:>60}".format("-->> Removing Employee <<--"))
    Id = input("Enter Employee Id: ")
    if (check_employee(Id) == False):
        print("Employee ID Doesn't Exists\nTry Again..")
        press = input("Press any key to continue..")
        Promote_Employ()
    else:
        #query to delete Employee 
        sql = 'delete from empdata where id = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Employee Removed!")
        press = input("Press any key to continue..")
        menu()

#Function to Search Employee
def Search_Employ():
    print("{:>60}".format("-->> Searching Employee <<--"))
    Id = input("Enter Employee Id: ")
    if (check_employee(Id) == False):
        print("Employee ID Doesn't Exists\nTry Again..")
        press = input("Press any key to continue..")
        Promote_Employ()
    else:
        sql = 'select * from empdata where Id = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        for i in r:
            print("Employee Id: ", i[0])
            print("Employee Name: ", i[1])
            print("Employee Email: ", i[2])
            print("Employee Phone: ", i[3])
            print("Employee Address: ", i[4])
            print("Employee Post: ", i[5])
            print("Employee Salary: ", i[6])
            print("\n")
        press = input("Press any key to continue..")
        menu()
        



# Function Menu

def menu():
    system("cls")
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Record")
    print("4. Promote Employee Record")
    print("5. Remove Employee Record")
    print("6. Search Employee Record")
    print("7. Exit\n")
    print("{:>60}".format("-->> Choose Options: [1/2/3/4/5/6/7] <<--"))

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        system("cls")
        Add_Employ()
    elif ch == 2:
        system("cls")
        Display_Employ()
    elif ch == 3:
        system("cls")
        Update_Employ()
    elif ch == 4:
        system("cls")
        Promote_Employ()
    elif ch == 5:
        system("cls")
        Remove_Employ()
    elif ch == 6:
        system("cls")
        Search_Employ()
    elif ch == 7:
        system("cls")
        print("{:>60}".format("Have a nice day :)"))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press any key to continue..")

menu()