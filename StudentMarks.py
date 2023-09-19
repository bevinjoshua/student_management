import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *


mysqldb = mysql.connector.connect(host="localhost", user="root", password="root")
mycursor = mysqldb.cursor()

mycursor.execute("create database if not exists student_management_system")
mycursor.execute("use student_management_system")
mycursor.execute("create table if not exists student_marks(id int auto_increment primary key,student_name varchar(255),subject_1 int,subject_2 int,subject_3 int,subject_4 int,subject_5 int)")


def Add():
    name = e1.get()
    subject_1 = e2.get()
    subject_2 = e3.get()
    subject_3 = e4.get()
    subject_4 = e5.get()
    subject_5 = e6.get()

    try:
        sql = "INSERT INTO student_marks(student_name,subject_1,subject_2,subject_3,subject_4,subject_5) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (name,subject_1,subject_2,subject_3,subject_4,subject_5)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Details Inserted Successfully...!!!")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def Get_data(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    id.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    id.insert(0,select['id'])
    e1.insert(0,select['Student Name'])
    e2.insert(0,select['Subject 1'])
    e3.insert(0,select['Subject 2'])
    e4.insert(0,select['Subject 3'])
    e5.insert(0,select['Subject 4'])
    e6.insert(0,select['Subject 5'])


def Update():
    stud_id = id.get()
    name = e1.get()
    subject_1 = e2.get()
    subject_2 = e3.get()
    subject_3 = e4.get()
    subject_4 = e5.get()
    subject_5 = e6.get()


    try:
        sql = "Update student_marks set student_name= %s, subject_1= %s, subject_2= %s, subject_3 = %s, subject_4= %s, subject_5= %s where id= %s"
        val = (name,subject_1,subject_2,subject_3,subject_4,subject_5, stud_id)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Details Updated Successfully...!!!")
        id.delete(0, END)
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def show():

    mycursor.execute("SELECT * FROM student_marks")
    data = mycursor.fetchall()
    print(data)

    for i, (id,student_name,subject_1,subject_2,subject_3,subject_4,subject_5) in enumerate(data, start=1):
        listBox.insert("", "end", values=(id,student_name,subject_1,subject_2,subject_3,subject_4,subject_5))
        mysqldb.close()

def Delete():
    stud_id = id.get()


    try:
        sql = "delete from student_marks where id= %s"
        val = (stud_id,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Deleted Successfully...!!!")

        id.delete(0, END)
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def ReportCard():
    t1.insert(END, '\t\tREPORT CARD' + '\n\n\n')
    t1.insert(END, '\tStudent Name         :   ' + e1.get() + '\n\n')
    t1.insert(END, '\tSubject 1            :   ' + e2.get() + '\n\n')
    t1.insert(END, '\tSubject 2            :   ' + e3.get() + '\n\n')
    t1.insert(END, '\tSubject 3            :   ' + e4.get() + '\n\n')
    t1.insert(END, '\tSubject 4            :   ' + e5.get() + '\n\n')
    t1.insert(END, '\tSubject 5            :   ' + e6.get() + '\n\n\n\n')

    x1 = int(e2.get()) + int(e3.get()) + int(e4.get()) + int(e5.get()) + int(e6.get())

    percentage = (x1 * 100) / 500

    if (x1 >= 451):
        Grade = 'A+'

    elif (x1 >= 401 and x1<=450):
        Grade = 'A'

    elif (x1 >= 351 and x1 <= 400):
        Grade = 'B'

    elif (x1 >= 301 and x1 <= 350):
        Grade = 'C'

    elif (x1 >= 201 and x1 <= 300):
        Grade = 'D'

    elif (x1 >= 175 and x1 <= 200):
        Grade = 'E'

    else:
        Grade = 'F'

    t1.insert(END, '\tTotal                :   ' + str(x1) + '\n')
    t1.insert(END, '\tGrade                :   ' + Grade + '\n')
    t1.insert(END, '\tPercentage           :   ' + str(percentage) +'%' '\n')

root = Tk()
root.geometry("1350x750")
root.config(bg='lightblue')
global e1
global e2
global e3
global e4
global e5
global e6
global id

tk.Label(root, text="Student Marks", bg="lightblue", fg="red", font=("Comic Sans MS", 30)).place(x=350, y=5)
Label(root, text="Student Name:", bg="lightblue").place(x=10, y=100)
Label(root, text="Subject 1:", bg="lightblue").place(x=10, y=140)
Label(root, text="Subject 2:", bg="lightblue").place(x=10, y=180)
Label(root, text="Subject 3:", bg="lightblue").place(x=10, y=220)
Label(root, text="Subject 4:", bg="lightblue").place(x=10, y=260)
Label(root, text="Subject 5:", bg="lightblue").place(x=10, y=300)

e1 = Entry(root, bg="pink")
e1.place(x=180, y=100)

e2 = Entry(root, bg="pink")
e2.place(x=180, y=140)

e3 = Entry(root, bg="pink")
e3.place(x=180, y=180)

e4 = Entry(root, bg="pink")
e4.place(x=180, y=220)

e5 = Entry(root, bg="pink")
e5.place(x=180, y=260)

e6 = Entry(root, bg="pink")
e6.place(x=180, y=300)

id = Entry(root, bg="pink")
id.place(x=1020, y=1020)

t1 = Text(root, width=80, height=20)
t1.grid(row=10, column=1)
t1.place(x=650, y=100)

Button(root, bg="pink", text="Add", command= Add, height=3, width=13).place(x=500, y=90)
Button(root, bg="Grey", text="Update", command= Update, height=3, width=13).place(x=500, y=150)
Button(root, bg="pink", text="Delete", command= Delete, height=3, width=13).place(x=500, y=210)
Button(root, bg="pink", text="ReportCard", command= ReportCard, height=3, width=13).place(x=500, y=210)

cols = ('id', 'Student Name', 'Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Subject 5')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, columns=8, columnspan=1)
    listBox.place(x=10, y=450)

show()
listBox.bind('<Double-Button-1>', Get_data)


root.mainloop()
