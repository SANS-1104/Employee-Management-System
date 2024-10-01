import pandas as pd

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1104",
  database = 'iimt'
)
cursor = mydb.cursor()


def addEmp(name, email, phone, salary, dept, post):
    addQ = "INSERT INTO employee (ename, email, phone, salary, department, post) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(addQ, (name, email, phone, salary, dept, post))
    mydb.commit()
    print('-'*50)
    print('Data Added Sucessfully!!')
    print('-'*50)

def viewEmp():
    viewQ = 'select * from employee'
    cursor.execute(viewQ)
    result = cursor.fetchall()
    print('-'*50)
    cols = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(result, columns=cols)
    print(df.to_string())
    print('-'*50)

def updatephone(eid,newval):
    updateQ = f'update employee set phone = %s where eid = %s'
    cursor.execute(updateQ,(newval,eid))
    mydb.commit()
    print('-'*50)
    print('Data Updated Sucessfully!')
    print('-'*50)


def  delEmp(eid):
    delQ = 'delete from employee where eid = %s'
    cursor.execute(delQ,(eid,))
    mydb.commit()
    print('-'*50)
    print('Employee Record Removed Sucessfully!')
    print('-'*50)



def promoteEmp(eid,newsal):
    updateQ = f'update employee set salary = %s where eid = %s'
    cursor.execute(updateQ,(newsal,eid))
    mydb.commit()
    print('-'*50)
    print('Employee Promoted Sucessfully!')
    print('-'*50)


ans = 'y'
while (ans == 'y'.lower()):
    print('-'*50)
    print('Employee Management System')
    print('-'*50)
    print('What do you want to do ? ')
    print('Press 1 : To View All Employee Records')
    print('Press 2 : To Add an Employee Data')
    print('Press 3 : To Update Employee phone')
    print('Press 4 : To Delete an Employee Record')
    print('Press 5 : To Promote an Employee')
    op = int(input('Enter you choice :'))
    
    if (op==1):
        viewEmp()
    elif (op==2):
        name = input('Employee Name :')
        email = input('Employee email :')
        phone = int(input('Employee Phone No. :'))
        salary = float(input('Employee Salary :'))
        dept = input('Employee Department :')
        post = input('Employee Post :')
        addEmp(name, email, phone, salary, dept, post)
    elif (op==3):
        eid = int(input('Enter Employee id : '))
        newval = int(input('Enter New Phone No: '))
        updatephone(eid,newval)
    elif (op==4):
        eid = int(input('Enter Employee id to delete : '))
        delEmp(eid)
    elif (op==5):
        eid = int(input('Enter Employee id : '))
        newsal = float(input('Enyer Employee New Salary : '))
        promoteEmp(eid,newsal)
         
    else:
        print('Invalid Option!')

    ans = input('Do you want to Continue ? [y/n]')

