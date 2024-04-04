from tkinter import *
import mysql.connector
cal = Tk()
cal.title("Simple Calculator")
cal.geometry("400x300+600+150")
cal.config(background="yellow")


F1 = Frame(cal)
F1.pack(padx=1, pady=1)

label1= Label(F1, text="Number1")
label1.place(x=10, y=20)

label2 = Label(F1, text="Number2")
label2.place(x=160, y=20)

E1 = Entry(F1)
E1.pack(padx=10, pady=50, side=LEFT)

E2 = Entry(F1)
E2.pack(padx=10, pady=50, side=RIGHT)

F2 = Frame(cal)
F2.pack(side=BOTTOM, pady=70)

def database(x,y,z):
    try:
    
      connection=mysql.connector.connect(host="localhost", database="caldb", user="root", password="")
      Query = "INSERT INTO calculations(number1,number2,sum) VALUES(%s,%s,%s)";
      data = (x,y,z)
      cursor= connection.cursor()
      cursor.execute(Query,data)
      print("Data is inserted successfully")
      connection.commit()
      cursor.close()
 
    except mysql.connector.Error as error:
     print("Mysql error is "+error)
    
    finally:
      if connection.is_connected():
         print("Connection is successfully established")
         connection.close()
def database1(x,y,z):
    try:
    
      connection=mysql.connector.connect(host="localhost", database="caldb", user="root", password="")
      Query = "INSERT INTO calculations(number1,number2,Substract) VALUES(%s,%s,%s)";
      data = (x,y,z)
      cursor= connection.cursor()
      cursor.execute(Query,data)
      print("Data is inserted successfully")
      connection.commit()
      cursor.close()
 
    except mysql.connector.Error as error:
     print(error)

    finally:
      if connection.is_connected():
         print("Connection is successfully established")
         connection.close()
def database2(x,y,z):
    try:
    
      connection=mysql.connector.connect(host="localhost", database="caldb", user="root", password="")
      Query = "INSERT INTO calculations(number1,number2,Multiply) VALUES(%s,%s,%s)";
      data = (x,y,z)
      cursor= connection.cursor()
      cursor.execute(Query,data)
      print("Data is inserted successfully")
      connection.commit()
      cursor.close()
 
    except mysql.connector.Error as error:
     print(error)

    finally:
      if connection.is_connected():
         print("Connection is successfully established")
         connection.close()
def database3(x,y,z):
    try:
    
      connection=mysql.connector.connect(host="localhost", database="caldb", user="root", password="")
      Query = "INSERT INTO calculations(number1,number2,Division) VALUES(%s,%s,%s)";
      data = (x,y,z)
      cursor= connection.cursor()
      cursor.execute(Query,data)
      print("Data is inserted successfully")
      connection.commit()
      cursor.close()
 
    except mysql.connector.Error as error:
     print(error)

    finally:
      if connection.is_connected():
         print("Connection is successfully established")
         connection.close()


def add():
    x = int(E1.get())
    y = int(E2.get())
    z = x+y
    label.config(text=str(z))
    print(z)
    database(x,y,z)
def substract():
    x = int(E1.get())
    y = int(E2.get())
    z = x-y
    label.config(text=str(z))
    print(z)
    database1(x,y,z)
def multiply():
    x = int(E1.get())
    y = int(E2.get())
    z = x*y
    label.config(text=str(z))
    print(z)
    database2(x,y,z)
def division():
    x = int(E1.get())
    y = int(E2.get())
    if(y>0):
     z = x / y

    else:
        label.config(text="Y cannot be zero")
    label.config(text=str(z))
    print(z)
    database3(x,y,z)

B1 = Button(F2, text="+", command=add)
B1.pack(side=LEFT, padx=10)
B1 = Button(F2, text="-", command=substract)
B1.pack(side=LEFT, padx=10)
B1 = Button(F2, text="*", command=multiply)
B1.pack(side=LEFT, padx=10)
B1 = Button(F2, text="/", command= division)
B1.pack(side=LEFT, padx=10)
label = Label(cal, text="0")
label.pack()



cal.mainloop()