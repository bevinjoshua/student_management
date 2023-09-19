import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

mysqldb = mysql.connector.connect(host="localhost", user="root", password="root")
mycursor = mysqldb.cursor()

mycursor.execute("create database if not exists student_management_system")
mycursor.execute("use student_management_system")
mycursor.execute("create table if not exists fee_details(id int auto_increment primary key,receipt_no varchar(30),student_name varchar(255),admission_no varchar(30),std varchar(30),total_amount varchar(30),paid_amount varchar(30))")


def Add():
    receipt_no = e1.get()
    student_name = e2.get()
    admission_no = e3.get()
    std = e4.get()
    total_amount = e5.get()
    paid_amount = e6.get()


    try:
        sql = "INSERT INTO fee_details(receipt_no,student_name,admission_no,std,total_amount,paid_amount) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (receipt_no,student_name,admission_no,std,total_amount,paid_amount)
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

def view():

    mycursor.execute("SELECT receipt_no, student_name, admission_no, std, total_amount, paid_amount FROM fee_details")
    data = mycursor.fetchall()
    print(data)

    for i, (receipt_no, student_name, admission_no, std, total_amount, paid_amount) in enumerate(data, start=1):
        listBox.insert("", "end", values=(receipt_no, student_name, admission_no, std, total_amount, paid_amount))
        mysqldb.close()


def Get_data(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)

    e1.insert(0, select['Receipt No'])
    e2.insert(0, select['Student Name'])
    e3.insert(0, select['Admission No'])
    e4.insert(0, select['Class'])
    e5.insert(0, select['Total Amount'])
    e6.insert(0, select['Paid Amount'])

def Receipt():
    t1.insert(END, '\t\tRECEIPT' + '\n\n\n')
    t1.insert(END, '\tReceipt No       :   ' + e1.get() + '\n\n')
    t1.insert(END, '\tStudent Name     :   ' + e2.get() + '\n\n')
    t1.insert(END, '\tAdmission No     :   ' + e3.get() + '\n\n')
    t1.insert(END, '\tClass            :   ' + e4.get() + '\n\n')
    t1.insert(END, '\tTotal Amount     :   ' + e5.get() + '\n\n')
    t1.insert(END, '\tPaid Amount      :   ' + e6.get() + '\n\n')

    x1 = int(e5.get()) - int(e6.get())

    t1.insert(END, '\tBalance Amount   :   ' + str(x1) + '\n')



root = Tk()
root.geometry("1350x750")
root.config(bg='lightblue')
global e1
global e2
global e3
global e4
global e5
global e6

tk.Label(root, text="Fee Details", bg="lightblue", fg="red", font=("Comic Sans MS", 30)).place(x=350, y=5)
Label(root, text="Receipt Number:", bg="lightblue", font=("Comic Sans MS", 10, "bold")).place(x=10, y=100)
Label(root, text="Student Name:", bg="lightblue", font=("Comic Sans MS", 10, "bold")).place(x=10, y=140)
Label(root, text="Admission Name:", bg="lightblue", font=("Comic Sans MS", 10, "bold")).place(x=10, y=180)
Label(root, text="Class:", bg="lightblue", font=("Comic Sans MS", 10, "bold")).place(x=10, y=220)
Label(root, text="Total Amount:", bg="lightblue", font=("Comic Sans MS", 10, "bold")).place(x=10, y=260)
Label(root, text="Paid Amount:", bg="lightblue", font=("Comic Sans MS", 10, "bold")).place(x=10, y=300)

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

t1 = Text(root, width=80, height=20)
t1.grid(row=10, column=1)
t1.place(x=650, y=100)

Button(root, bg="pink", text="Add", command= Add, height=3, width=13).place(x=500, y=150)
Button(root, bg="pink", text="Receipt", command= Receipt, height=3, width=13).place(x=500, y=250)

cols = ('Receipt No', 'Student Name', 'Admission No', 'Class', 'Total Amount', 'Paid Amount')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, columns=8, columnspan=1)
    listBox.place(x=10, y=450)

view()
listBox.bind('<Double-Button-1>', Get_data)


root.mainloop()
