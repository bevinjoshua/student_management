import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

mysqldb = mysql.connector.connect(host="localhost", user="root", password="root")
mycursor = mysqldb.cursor()

mycursor.execute("create database if not exists student_management_system")
mycursor.execute("use student_management_system")
mycursor.execute("create table if not exists student_details(id int auto_increment primary key,name varchar(255),roll_no varchar(30),address varchar(255),phone_number varchar(30),std varchar(10),father_name varchar(255))")

def Add():
    name = e1.get()
    roll_no = e2.get()
    address = e3.get()
    phone_number = e4.get()
    std = e5.get()
    father_name = e6.get()

    try:
        sql = "INSERT INTO student_details(name,roll_no,address,phone_number,std,father_name) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (name,roll_no,address,phone_number,std,father_name)
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
    e2.insert(0,select['Roll No'])
    e3.insert(0,select['Address'])
    e4.insert(0,select['Phone Number'])
    e5.insert(0,select['Class'])
    e6.insert(0,select['Father Name'])


def Update():
    stud_id = id.get()
    name = e1.get()
    roll_no = e2.get()
    address = e3.get()
    phone_number = e4.get()
    std = e5.get()
    father_name = e6.get()

    try:
        sql = "Update student_details set name= %s, roll_no= %s, address= %s, phone_number = %s, std= %s, father_name= %s where id= %s"
        val = (name, roll_no, address, phone_number, std, father_name, stud_id)
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

    mycursor.execute("SELECT * FROM student_details")
    data = mycursor.fetchall()
    print(data)

    for i, (id, name, roll_no, address, phone_number, std, father_name) in enumerate(data, start=1):
        listBox.insert("", "end", values=(id, name, roll_no, address, phone_number, std, father_name))
        mysqldb.close()

def Delete():
    stud_id = id.get()

    try:
        sql = "delete from student_details where id= %s"
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

tk.Label(root, text="Student Details", bg="lightblue", fg="red", font=("Comic Sans MS", 30)).place(x=350, y=5)
Label(root, text="Student name:", bg="lightblue").place(x=10, y=100)
Label(root, text="Roll No:", bg="lightblue").place(x=10, y=140)
Label(root, text="Address:", bg="lightblue").place(x=10, y=180)
Label(root, text="Phone Number:", bg="lightblue").place(x=10, y=220)
Label(root, text="Class:", bg="lightblue").place(x=10, y=260)
Label(root, text="Father's Name:", bg="lightblue").place(x=10, y=300)

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

Button(root, bg="pink", text="Add", command= Add, height=3, width=13).place(x=800, y=90)
Button(root, bg="Grey", text="Update", command= Update, height=3, width=13).place(x=800, y=150)
Button(root, bg="pink", text="Delete", command= Delete, height=3, width=13).place(x=800, y=210)

cols = ('id', 'Student Name', 'Roll No', 'Address', 'Phone Number', 'Class', 'Father Name')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, columns=8, columnspan=1)
    listBox.place(x=10, y=400)

show()
listBox.bind('<Double-Button-1>', Get_data)


root.mainloop()
