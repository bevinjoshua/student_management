from tkinter import *
import random
import os


def StudentDetails():
    filename = 'StudentManagementSystem.py'
    os.system(filename)


def FeeReport():
    filename = 'FeeReport.py'
    os.system(filename)

def StudentMarks():
    filename = 'StudentMarks.py'
    os.system(filename)


root = Tk()
root.title('Menu')
root.geometry('1350x750')

title_Frame = LabelFrame(root, font=('arial', 50, 'bold'), width=1000, height=100, bg='lightblue', relief='raise',
                             bd=13)
title_Frame.grid(row=0, column=0, pady=50)

title_Label = Label(title_Frame, text='School Management System', font=('arial', 30, 'bold'), bg='lightblue')
title_Label.grid(row=0, column=0, padx=150)


Frame_1 = LabelFrame(root, font=('arial', 17, 'bold'), width=1000, height=100, bg='lightblue', relief='ridge',bd=10)
Frame_1.grid(row=1, column=0, padx=280)
Frame_2 = LabelFrame(root, font=('arial', 17, 'bold'), width=1000, height=100, bg='lightblue', relief='ridge',bd=10)
Frame_2.grid(row=2, column=0, padx=130, pady=7)
Frame_3 = LabelFrame(root, font=('arial', 17, 'bold'), width=1000, height=100, bg='lightblue', relief='ridge',bd=10)
Frame_3.grid(row=3, column=0, padx=130, pady=7)


Label_1 = Label(Frame_1, text='STUDENT PROFILE', font=('arial', 25, 'bold'), bg='lightblue')
Label_1.grid(row=0, column=0, padx=50, pady=5)
Label_2 = Label(Frame_2, text='FEE REPORT', font=('arial', 25, 'bold'), bg='lightblue')
Label_2.grid(row=0, column=0, padx=100, pady=5)
Label_3 = Label(Frame_3, text='STUDENT MARKS', font=('arial', 25, 'bold'), bg='lightblue')
Label_3.grid(row=0, column=0, padx=100, pady=5)


Button_1 = Button(Frame_1, text='VIEW', font=('arial', 16, 'bold'), width=8, command=StudentDetails)
Button_1.grid(row=0, column=3, padx=50)
Button_2 = Button(Frame_2, text='VIEW', font=('arial', 16, 'bold'), width=8, command=FeeReport)
Button_2.grid(row=0, column=3, padx=50)
Button_3 = Button(Frame_3, text='VIEW', font=('arial', 16, 'bold'), width=8, command=StudentMarks)
Button_3.grid(row=0, column=3, padx=50)

root.mainloop()