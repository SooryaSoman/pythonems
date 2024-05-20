import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='soorya123#',
    database='ems'
)
cursor=mydb.cursor()
while(True):
    print("*******************")
    print('1.Insert Employee')
    print('2.View')
    print('3.Search')
    print('4.Delete')
    print('5.Update')
    print('6.Exit')
    print("*******************")
    choice=int(input('enter your choice'))
    if choice == 1:
        #Insert
        print('Enter the employee details')
        id=int(input('enter the employee id'))
        name=(input('enter the employee name'))
        salary=float(input('enter the employee salary'))
        dept=(input('enter the employee dept'))
        query="insert into employee values (%s, %s, %s, %s)"
        values=(id,name,salary,dept)
        cursor.execute(query,values)
        mydb.commit()
        print("employee added successfully")
    elif choice == 2:
        #View
      cursor.execute("select* from employee")
      rows=cursor.fetchall()
      for row in rows:
        print("Employee id:",row[0])
        print("Employee name:",row[1])
        print("Employee salary:",row[2])
        print("Employee dept:",row[3])
    elif  choice == 3:
        name=(input('enter the employee name to be searched'))
        query=f'select * from employee where emp_name like"%{name}%"'
        cursor.execute(query)
        rows=cursor.fetchall()
        for row in rows:
         print("Employee id:",row[0])
         print("Employee name:",row[1])
         print("Employee salary:",row[2])
         print("Employee dept:",row[3])
    elif  choice == 4:    
        emp_id=int(input('enter the employee id to be deleted'))
        query="DELETE FROM  employee WHERE emp_id = %s"
        value=(emp_id,) 
        cursor.execute(query,value )
        mydb.commit()
        print("employee deleted successfully") 
    elif  choice == 5:    
        emp_id=int(input('enter the employee id'))
        new_salary=float(input('enter the new employee salary'))
        query="UPDATE employee SET emp_salary=%s where emp_id=%s"
        values=(new_salary,emp_id) 
        cursor.execute(query,values) 
        mydb.commit()
        print("employee updated successfully")  
    elif  choice == 6:    
        print('Exiting')    
        break
    else:
        print("invalid choice")