from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import mysql.connector as con
    
def ok():
    messagebox.showinfo("Done","Account Created")


def staff():
    staff=Tk()
    staff.geometry("700x500")
    staff.title("STAFF LOGIN")
    staff.iconbitmap(r'C:\Users\MANJU\AppData\Local\Programs\Python\Python39\favicon.ico')
    staff1=Label(staff,text="Phones 4 U",
               font=("algerian",50,"bold"),fg="black")
    staff1.grid(row=0,column=2)

    staffusername=Label(staff,text="Your Username:",font=("calibri",25),fg="black")
    staffusername.grid(row=2,column=1)

    staffpassword=Label(staff,text="Password:",font=("calibri",25),fg="black")
    staffpassword.grid(row=3,column=1)

    staffeuname=Entry(staff,font=("calibri",25),bd=10) 
    staffeuname.grid(row=2,column=2)

    staffepass=Entry(staff,font=("calibri",25),bd=10,show="*")
    staffepass.grid(row=3,column=2)

    Button5=Button(staff,text="Login",fg="black",cursor="hand2",font=("calidri",10),bg="yellow")
    Button5.grid(row=5,column=2)

    staffunq=Label(staff,text="Unique Number:",font=("calibri",25),fg="black")
    staffunq.grid(row=1,column=1)

    staffunqe=Entry(staff,font=("calibri",25),bd=10) 
    staffunqe.grid(row=1,column=2)

    
def New():
    New=Tk()
    New.geometry("700x500")
    New.title("New Account")
    New.iconbitmap(r'C:\Users\MANJU\AppData\Local\Programs\Python\Python39\favicon.ico')
    NewName=Label(New,text="Phones 4 U",
               font=("algerian",50,"bold"),fg="black")
    NewName.grid(row=0,column=2)

    Newusername=Label(New,text="Your New Username:",font=("calibri",25),fg="black")
    Newusername.grid(row=1,column=1)

    Newpassword=Label(New,text="Password:",font=("calibri",25),fg="black")
    Newpassword.grid(row=2,column=1)

    Neweuname=Entry(New,font=("calibri",25),bd=10) 
    Neweuname.grid(row=1,column=2)

    Newepass=Entry(New,font=("calibri",25),bd=10,show="*")
    Newepass.grid(row=2,column=2)

    Newpassword1=Label(New,text="Re-Enter Password:",font=("calibri",25),fg="black")
    Newpassword1.grid(row=3,column=1)

    Newepass1=Entry(New,font=("calibri",25),bd=10,show="*")
    Newepass1.grid(row=3,column=2)

    Button3=Button(New,text="Create Account",fg="black",cursor="hand2",font=("calidri",10),bg="yellow",command=ok)
    Button3.grid(row=4,column=2)



login=Tk()
login.geometry("700x500")
login.title("Project")
login.iconbitmap(r'C:\Users\MANJU\AppData\Local\Programs\Python\Python39\favicon.ico')
Name=Label(login,text="Phones 4 U",font=("algerian",50,"bold"),fg="black")
Name.grid(row=0,column=2)

username=Label(login,text="Username:",font=("calibri",25),fg="black")
username.grid(row=1,column=1)

password=Label(login,text="Password:",font=("calibri",25),fg="black")
password.grid(row=2,column=1)


euname=Entry(login,font=("calibri",25),bd=10)
euname.grid(row=1,column=2)

epass=Entry(login,font=("calibri",25),bd=10,show="*")
epass.grid(row=2,column=2)

Button1=Button(login,text="Create Account",fg="black",font=("calidri",10),bg=None,cursor="hand2",command=New)
Button1.grid(row=3,column=1)

Button2=Button(login,text="Login",fg="black",font=("calidri",10),bg="Yellow",cursor="hand2")
Button2.grid(row=3,column=2)

Button4=Button(login,text="      STAFF      ",fg="black",font=("calidri",10),bg=None,cursor="hand2",command=staff)
Button4.grid(row=3,column=3)
