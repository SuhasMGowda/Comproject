from tkinter import *
from tkinter import messagebox



import mysql.connector as con



mycon = con.connect(host='localhost', user='root', passwd='admin@123')


#CREATING DATABASE
l=mycon.cursor()

w="Create  database IF NOT EXISTS WILDLIFE"

v=l.execute(w)

p="Use WILDLIFE"

l.execute(p)

#CREATING TABLES INFO AND LOGIN


a= "Create table IF NOT EXISTS login(USERNAME varchar(20),PASSWORD varchar(20))"

c=l.execute(a)

b="Create table IF NOT EXISTS DATA(SL_NO INT AUTO_INCREMENT PRIMARY KEY,SPECIES varchar(30),ORIGIN varchar(20),AGE int(10),BREED varchar(20),VACCINATION varchar(5))"
d=l.execute(b)

def ok():
    messagebox.showinfo("Done","Account Created")

def Neww():
    global New
    New=Tk()
    New.config(bg='honeydew3')
    New.geometry("1100x450")
    New.title("New Account")

    global NewName
    NewName=Label(New,text="Wildlife Rescuer",
               font=("algerian",50,"bold"),fg="black",bg="honeydew3")
    NewName.grid(row=0,column=2)

    Newusername=Label(New,text="Your New Username:",font=("calibri",25),fg="black",bg="honeydew3")
    Newusername.grid(row=1,column=1)
    
    global Newpass
    Newpassword=Label(New,text="Password:",font=("calibri",25),fg="black",bg="honeydew3")
    Newpassword.grid(row=2,column=1)
    
    global Neweuname
    Neweuname=Entry(New,font=("calibri",25),bd=10) 
    Neweuname.grid(row=1,column=2)
    
    global newname
    newname = Neweuname.get()
    global Newepass
    Newepass=Entry(New,font=("calibri",25),bd=10,show="*")
    Newepass.grid(row=2,column=2)
    

    global Newpass1
    Newpassword1=Label(New,text="Re-Enter Password:",font=("calibri",25),fg="black",bg="honeydew3")
    Newpassword1.grid(row=3,column=1)

    global Newepass1
    Newepass1=Entry(New,font=("calibri",25),bd=10,show="*")
    Newepass1.grid(row=3,column=2)
    

    Button3=Button(New,text="Create Account",fg="black",cursor="hand2",font=("calidri",10),command=check_user,bg="light blue",padx=40,pady=10)
    Button3.grid(row=4,column=2)
    New.mainloop()

def check_pass():
    if Newepass.get() == Newepass1.get():
        userr = Neweuname.get()
        passs = Newepass.get()
        cur = mycon.cursor()
        a = "INSERT INTO login value('{}','{}')".format(userr,passs)
        cur.execute(a)
        mycon.commit()
        ok()
        New.destroy()
        mycon.commit()

        
        
        
        
        

    else:
        messagebox.showwarning("ERROR","Passwords dont match! Try again")
        New.destroy()
        Neww()
        
        
    

def check_user():
        if not Neweuname.get():
            messagebox.showwarning("ERROR","You didnt enter username!")
            New.destroy()
            Neww()
        else:
            check_pass()
       
        
            
      

def loginn():
    i = mycon.cursor()
    un = euname.get()
   
    c = "SELECT * from login WHERE USERNAME = '{}'".format(un)
    i.execute(c)
    result = i.fetchall()
    if not result:
        messagebox.showwarning("ERROR","USERNAME DOESNT EXIST")
        loggin.destroy()
        loogin()

    else:
        passs = epass.get()
        if result[0][1] == passs:
            messagebox.showinfo("login", "LOGIN SUCCESSFULL")
            loggin.destroy()
            home()
        else:
            messagebox.showwarning("ERROR","INCORRECT PASSWORD")
            loggin.destroy()
            loogin()
    

def home():
    global login
    login=Tk()
    login.geometry("1000x400")
    login.config(bg='honeydew3')
    login.title("HOME")
    Name=Label(login,text="Wildlife Rescuer",font=("algerian",25,"bold"),fg="black",bg='honeydew3')
    Name.grid(row=0,column=0)

    logoutbut=Button(login,text='Logout',fg="black",cursor="hand2",font=("calidri",10),bg="OrangeRed2",padx=20,pady=10,command = log_out)
    logoutbut.grid(row=0,column=5)

    abc=Button(login,text='ADD DATA',font=('lato',20),fg='blue',height=2,width=15, relief = RAISED,command=show1)
    abc.grid(row=1,column=0,padx=20,pady=20)

    defg=Button(login,text='SHOW DATA',font=('lato',20),fg='blue',height=2,width=15, relief = RAISED, command = display)
    defg.grid(row=1,column=1,padx=20,pady=20)

    hijk=Button(login,text='SEARCH',font=('lato',20),fg='blue',height=2,width=15, relief = RAISED, command = search)
    hijk.grid(row=1,column=2,padx=20,pady=20)

    lmn=Button(login,text='EDIT DATA',font=('lato',20),fg='blue',height=2,width=15, relief = RAISED, command = modify)
    lmn.grid(row=2,column=0,padx=20,pady=20)

    opq=Button(login,text='DELETE DATA',font=('lato',20),fg='blue',height=2,width=15, relief = RAISED, command = deletee)
    opq.grid(row=2,column=1,padx=20,pady=20)

    rst=Button(login,text='DELETE ALL DATA',font=('lato',20),fg='blue',height=2,width=15, relief = RAISED, command = deletee_all)
    rst.grid(row=2,column=2,padx=20,pady=20)


    login.mainloop()

def show1():
    login.destroy()
    global frame1
    frame1=Tk()
    frame1.geometry('1000x400')
    frame1.title('ACCEPT')
    
    spec=Label(frame1,text="Species",font=("calibri",25))
    spec.grid(row=1,column=0)
    
    global specet
    specet=Entry(frame1,font=("calibri",25), bd = 5)
    specet.grid(row=1,column=1)
    
    orig=Label(frame1,text="Origin",font=("calibri",25))
    orig.grid(row=2,column=0)
    
    global origet
    origet=Entry(frame1,font=("calibri",25), bd = 5 )
    origet.grid(row=2,column=1)
    
    age=Label(frame1,text="Age",font=("calibri",25))
    age.grid(row=3,column=0)
    
    global ageet
    ageet=Entry(frame1,font=("calibri",25), bd = 5)
    ageet.grid(row=3,column=1)
    
    breed=Label(frame1,text="Breed",font=("calibri",25))
    breed.grid(row=4,column=0)
    
    global breedet
    breedet=Entry(frame1,font=("calibri",25), bd = 5)
    breedet.grid(row=4,column=1)
    
    vaci=Label(frame1,text="Vaccination Status",font=("calibri",25))
    vaci.grid(row=5,column=0)

    options_list = ["Yes", "No"]
    global value_inside
    value_inside = StringVar(frame1)
    value_inside.set("Select an Option")
    question_menu = OptionMenu(frame1, value_inside, *options_list)
    question_menu.grid(row=5, column = 1)
    
    
   
    
    acptet=Button(frame1,text='Add',font=('Calibri',10), bg='light blue', padx = 25, pady = 2, command = accept)
    acptet.grid(row=6,column=1)
    
    bacck = Button(frame1,text='BACK',font=('Calibri',10),bg='light blue', padx = 25, pady = 2, command = back_home)
    bacck.grid(row=7,column=1)

def back_home():
    frame1.destroy()
    home()

def accept():
    a,b,c,d,e = specet.get(), origet.get(), ageet.get(), breedet.get(), value_inside.get()
    inf = (a, b, c, d, e)
    ins = 'insert into data(species, origin, age, breed, vaccination) values(%s,%s,%s,%s,%s)'

    k = mycon.cursor()
    k.execute(ins, inf)
    mycon.commit()


    messagebox.showinfo('ACCEPTED', 'DATA ADDED SUCCESSFULLLY')
    frame1.destroy()
    home()



def display():
    mycursor = mycon.cursor()
    mycursor.execute("SELECT * FROM data")
    fet = mycursor.fetchall()  
    
    if not fet:
        messagebox.showwarning('EMPTY', 'NO DATA EXISTS!!')
    else:
        tablee = Tk()
        tablee.title("DATA")
        i=1
        for student in fet: 
            for j in range(len(student)):
                e = Entry(tablee, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, student[j])
            i=i+1
        ncci=Label(tablee,text="S.No",width=10,fg='blue')
        ncci.grid(row=0,column=0)
        ncci1=Label(tablee,text="Species",width=10,fg='blue')
        ncci1.grid(row=0,column=1)
        ncci2=Label(tablee,text="Origin",width=10,fg='blue')
        ncci2.grid(row=0,column=2)
        ncci3=Label(tablee,text="Age",width=10,fg='blue')
        ncci3.grid(row=0,column=3)
        ncci4=Label(tablee,text="Breed",width=10,fg='blue')
        ncci4.grid(row=0,column=4)
        ncci5=Label(tablee,text="Vaccination",width=10,fg='blue')
        ncci5.grid(row=0,column=5)
        tablee.mainloop() 


def deletee_all():
    mycursor = mycon.cursor()
    mycursor.execute("drop table data")
    messagebox.showinfo('DONE', 'DATA WIPED OUT!!')
    mycon.commit()
    
    b="Create table IF NOT EXISTS DATA(SL_NO INT AUTO_INCREMENT PRIMARY KEY,SPECIES varchar(30),ORIGIN varchar(20),AGE int(10),BREED varchar(20),VACCINATION varchar(5))"
    l.execute(b)
    mycon.commit()



def search():
    global sear
    sear = Tk()
    sear.title("SEARCH")
    sear.geometry('1000x400')
    options_list = ["species", "origin", "age", "breed", "vaccination status"]
    value_inside = StringVar(sear)
    value_inside.set("Select an Option")
    question_menu = OptionMenu(sear, value_inside, *options_list)
    question_menu.pack()
    def spec():
        if value_inside.get() == 'species':
            namee = Label(sear, text = 'Enter the species you want to search', font=("calibri",25))
            namee.pack()
          
            name = Entry(sear, width=10, fg='blue', font = ('Calibri', 25))
            name.pack()
            def diss():
               
                cursor = mycon.cursor()
                qry = "select * from data where SPECIES ='{}'".format(name.get())
                cursor.execute(qry)
                out = cursor.fetchall()
                if not out:
                    messagebox.showwarning('EMPTY', 'SPECIES "{}" NOT FOUND!'.format(name.get()))
                    sear.destroy()
                else:
                    sear.destroy()
                    tablee = Tk()
                    i=1
                    for student in out: 
                        for j in range(len(student)):
                            e = Entry(tablee, width=10, fg='blue') 
                            e.grid(row=i, column=j) 
                            e.insert(END, student[j])
                        i=i+1
                    ncci=Label(tablee,text="S.No",width=10,fg='blue')
                    ncci.grid(row=0,column=0)
                    ncci1=Label(tablee,text="Species",width=10,fg='blue')
                    ncci1.grid(row=0,column=1)
                    ncci2=Label(tablee,text="Origin",width=10,fg='blue')
                    ncci2.grid(row=0,column=2)
                    ncci3=Label(tablee,text="Age",width=10,fg='blue')
                    ncci3.grid(row=0,column=3)
                    ncci4=Label(tablee,text="Breed",width=10,fg='blue')
                    ncci4.grid(row=0,column=4)
                    ncci5=Label(tablee,text="Vaccination",width=10,fg='blue')
                    ncci5.grid(row=0,column=5)   
                    tablee.mainloop()
                
                

                
            specbut = Button(sear, text = 'search', font=('Calibri',10) ,bg='light blue', command = diss, padx = 5) 
            specbut.pack()
        
        elif value_inside.get() == 'origin':
            originn = Label(sear, text = 'Enter the origin you want to search', font=("calibri",25))
            originn.pack()
            origin = Entry(sear, width=10, fg='blue', font = ('Calibri', 25) )
            origin.pack()
            def dis_ori():
                qry = "select * from data where origin ='{}'".format(origin.get())
                cursor = mycon.cursor()
                cursor.execute(qry)
                out = cursor.fetchall()
                if not out:
                    messagebox.showwarning('EMPTY', 'ORIGIN "{}" NOT FOUND!'.format(origin.get()))
                    sear.destroy()
                else:
                    sear.destroy()
                    tablee = Tk()
                    i=1
                    for student in out: 
                        for j in range(len(student)):
                            e = Entry(tablee, width=10, fg='blue') 
                            e.grid(row=i, column=j) 
                            e.insert(END, student[j])
                        i=i+1
                    ncci=Label(tablee,text="S.No",width=10,fg='blue')
                    ncci.grid(row=0,column=0)
                    ncci1=Label(tablee,text="Species",width=10,fg='blue')
                    ncci1.grid(row=0,column=1)
                    ncci2=Label(tablee,text="Origin",width=10,fg='blue')
                    ncci2.grid(row=0,column=2)
                    ncci3=Label(tablee,text="Age",width=10,fg='blue')
                    ncci3.grid(row=0,column=3)
                    ncci4=Label(tablee,text="Breed",width=10,fg='blue')
                    ncci4.grid(row=0,column=4)
                    ncci5=Label(tablee,text="Vaccination",width=10,fg='blue')
                    ncci5.grid(row=0,column=5)
                    tablee.mainloop() 
            specbut = Button(sear, text = 'search', font=('Calibri',10), padx = 5,bg='light blue', command = dis_ori) 
            specbut.pack()

        elif value_inside.get() == 'age':
            agee = Label(sear, text = 'Enter the age of the animal you want to search', font=("calibri",25))
            agee.pack()
            age = Entry(sear, width=10, fg='blue', font = ('Calibri', 25))
            age.pack()
            def dis_age():
                qry = "select * from data where age ={}".format(age.get())
                cursor = mycon.cursor()
                cursor.execute(qry)
                out = cursor.fetchall()
                if not out:
                    messagebox.showwarning('EMPTY', 'AGE {} NOT FOUND!'.format(age.get()))
                    sear.destroy()
                else:
                    sear.destroy()
                    tablee = Tk()
                    i=1
                    for student in out: 
                        for j in range(len(student)):
                            e = Entry(tablee, width=10, fg='blue') 
                            e.grid(row=i, column=j) 
                            e.insert(END, student[j])
                        i=i+1
                    ncci=Label(tablee,text="S.No",width=10,fg='blue')
                    ncci.grid(row=0,column=0)
                    ncci1=Label(tablee,text="Species",width=10,fg='blue')
                    ncci1.grid(row=0,column=1)
                    ncci2=Label(tablee,text="Origin",width=10,fg='blue')
                    ncci2.grid(row=0,column=2)
                    ncci3=Label(tablee,text="Age",width=10,fg='blue')
                    ncci3.grid(row=0,column=3)
                    ncci4=Label(tablee,text="Breed",width=10,fg='blue')
                    ncci4.grid(row=0,column=4)
                    ncci5=Label(tablee,text="Vaccination",width=10,fg='blue')
                    ncci5.grid(row=0,column=5)
                    tablee.mainloop() 
            specbut = Button(sear, text = 'search', font=('Calibri',10), padx = 5,bg='light blue', command = dis_age) 
            specbut.pack()

        elif value_inside.get() == 'breed':
            breedd = Label(sear, text = 'Enter the breed you want to search', font=("calibri",25))
            breedd.pack()
            breed = Entry(sear, width=10, fg='blue', font = ('Calibri', 25))
            breed.pack()
            def dis_bri():
                qry = "select * from data where breed ='{}'".format(breed.get())
                cursor = mycon.cursor()
                cursor.execute(qry)
                out = cursor.fetchall()
                if not out:
                    messagebox.showwarning('EMPTY', 'BREED "{}" NOT FOUND!'.format(breed.get()))
                    sear.destroy()
                else:
                    sear.destroy()
                    tablee = Tk()
                    i=1
                    for student in out: 
                        for j in range(len(student)):
                            e = Entry(tablee, width=10, fg='blue') 
                            e.grid(row=i, column=j) 
                            e.insert(END, student[j])
                        i=i+1
                    ncci=Label(tablee,text="S.No",width=10,fg='blue')
                    ncci.grid(row=0,column=0)
                    ncci1=Label(tablee,text="Species",width=10,fg='blue')
                    ncci1.grid(row=0,column=1)
                    ncci2=Label(tablee,text="Origin",width=10,fg='blue')
                    ncci2.grid(row=0,column=2)
                    ncci3=Label(tablee,text="Age",width=10,fg='blue')
                    ncci3.grid(row=0,column=3)
                    ncci4=Label(tablee,text="Breed",width=10,fg='blue')
                    ncci4.grid(row=0,column=4)
                    ncci5=Label(tablee,text="Vaccination",width=10,fg='blue')
                    ncci5.grid(row=0,column=5)
                    tablee.mainloop() 
                 
            specbut = Button(sear, text = 'search', font=('Calibri',10), padx = 5,bg='light blue', command = dis_bri) 
            specbut.pack()

        elif value_inside.get() == 'vaccination status':
            vacc = Label(sear, text = 'Enter yes or no to search based on vaccination status', font=("calibri",25))
            vacc.pack()
            vacci= Entry(sear, width=10, fg='blue', font = ('Calibri', 25) )
            vacci.pack()
            def dis_vaci():
                qry = "select * from data where vaccination  ='{}'".format(vacci.get())
                cursor = mycon.cursor()
                cursor.execute(qry)
                out = cursor.fetchall()
                if not out:
                    messagebox.showwarning('EMPTY', 'NO ANIMAL FOUND WITH VACCINATION STATUS "{}"'.format(vacci.get()))
                    sear.destroy()
                else:
                    sear.destroy()
                    tablee = Tk()
                    i=1
                    for student in out: 
                        for j in range(len(student)):
                            e = Entry(tablee, width=10, fg='blue') 
                            e.grid(row=i, column=j) 
                            e.insert(END, student[j])
                        i=i+1
                    ncci=Label(tablee,text="S.No",width=10,fg='blue')
                    ncci.grid(row=0,column=0)
                    ncci1=Label(tablee,text="Species",width=10,fg='blue')
                    ncci1.grid(row=0,column=1)
                    ncci2=Label(tablee,text="Origin",width=10,fg='blue')
                    ncci2.grid(row=0,column=2)
                    ncci3=Label(tablee,text="Age",width=10,fg='blue')
                    ncci3.grid(row=0,column=3)
                    ncci4=Label(tablee,text="Breed",width=10,fg='blue')
                    ncci4.grid(row=0,column=4)
                    ncci5=Label(tablee,text="Vaccination",width=10,fg='blue')
                    ncci5.grid(row=0,column=5)
                    tablee.mainloop() 
                
            specbut = Button(sear, text = 'search', font=('Calibri',10), padx = 5,bg='light blue', command = dis_vaci) 
            specbut.pack()

        else:
            messagebox.showwarning('error', 'please choose an option from dropdown menu!!')
            sear.destroy()
            search()
    submit_button = Button(sear, text='Submit', command=spec, font = ('Calibri', 15))
    submit_button.pack()
    sear.mainloop()

def deletee():
    dell = Tk()
    dell.title("DELETE DATA")
    dell.geometry('1000x400')
    options_list = ["species", "origin", "age", "breed", "vaccination status"]
    value_inside = StringVar(dell)
    value_inside.set("Select an Option")
    question_menu = OptionMenu(dell, value_inside, *options_list)
    question_menu.pack()

    def spec_DEL():

        if value_inside.get() == 'species':
            nameeu = Label(dell, text = 'Enter the species you want to delete', font=("calibri",25))
            nameeu.pack()
          
            nam = Entry(dell, width=10, fg='blue', font = ('Calibri', 25) )
            nam.pack()
            def dil():
                
                cursor = mycon.cursor()
                qry1 = "select * from data where SPECIES ='{}'".format(nam.get())
                cursor.execute(qry1)
                out = cursor.fetchall()

                if not out:
                    messagebox.showwarning('EMPTY', 'SPECIES "{}" NOT FOUND!'.format(nam.get()))
                    dell.destroy()
                else:
                    qry = "Delete from data where SPECIES ='{}'".format(nam.get())
                    cursor.execute(qry)
                    mycon.commit()
                    messagebox.showinfo('done', 'deleted!!')
                    dell.destroy()
            
            specbut = Button(dell, text = 'delete', font=('Calibri',10), padx = 5,bg='light blue', command = dil) 
            specbut.pack()

        elif value_inside.get() == 'origin':
            orig = Label(dell, text = 'Enter the origin of the species you want to delete', font=("calibri",25))
            orig.pack()
          
            origin = Entry(dell, width=10, fg='blue', font = ('Calibri', 25) )
            origin.pack()
            def dil():
                
                cursor = mycon.cursor()
                qry1 = "select * from data where ORIGIN ='{}'".format(origin.get())
                cursor.execute(qry1)
                out = cursor.fetchall()
                if not out:
                    messagebox.showwarning('EMPTY', 'ORIGIN "{}" NOT FOUND!'.format(origin.get()))
                    dell.destroy()
                else:
                    qry = "Delete from data where ORIGIN ='{}'".format(origin.get())
                    cursor.execute(qry)
                    mycon.commit()
                    messagebox.showinfo('done', 'deleted!!')
                    dell.destroy()
                
            specbut = Button(dell, text = 'delete', font=('Calibri',10), padx = 5,bg='light blue', command = dil) 
            specbut.pack()

        
        elif value_inside.get() == 'age':
            agee = Label(dell, text = 'Enter the age of the species you want to delete', font=("calibri",25))
            agee.pack()
          
            age = Entry(dell, width=10, fg='blue', font = ('Calibri', 25))
            age.pack()
            def dil():
                
                cursor = mycon.cursor()
                qry1 = "select * from data where AGE ={}".format(age.get())
                cursor.execute(qry1)
                out = cursor.fetchall()
                if not out:
                    messagebox.showwarning('EMPTY', 'AGE {} NOT FOUND!'.format(age.get()))
                    dell.destroy()
                else:
                    qry = "Delete from data where AGE ={}".format(age.get())
                    cursor.execute(qry)
                    mycon.commit()
                    messagebox.showinfo('done', 'deleted!!')
                    dell.destroy()
                
            specbut = Button(dell, text = 'delete', font=('Calibri',10), padx = 5,bg='light blue', command = dil) 
            specbut.pack()

        
        elif value_inside.get() == 'breed':
            bred = Label(dell, text = 'Enter the breed you want to delete', font=("calibri",25))
            bred.pack()
          
            breed = Entry(dell, width=10, fg='blue', font = ('Calibri', 25) )
            breed.pack()
            def dil():
                
                cursor = mycon.cursor()
                qry1 = "select * from data where BREED='{}'".format(breed.get())
                cursor.execute(qry1)
                out = cursor.fetchall()
                if not out:
                    messagebox.showwarning('EMPTY', 'BREED "{}" NOT FOUND!'.format(breed.get()))
                    dell.destroy()
                else:
                    qry = "Delete from data where BREED ='{}'".format(breed.get())
                    cursor.execute(qry)
                    mycon.commit()
                    messagebox.showinfo('done', 'deleted!!')
                    dell.destroy()
                
            specbut = Button(dell, text = 'delete',font=('Calibri',10), padx = 5,bg='light blue', command = dil) 
            specbut.pack()
        
        
        elif value_inside.get() == 'vaccination status':
            vaa = Label(dell, text = 'Enter the vaccination status of the animals you want to delete', font=("calibri",25))
            vaa.pack()
           
            va = Entry(dell, width=10, fg='blue', font = ('Calibri', 25) )
            va.pack()
            def dil():
                
                cursor = mycon.cursor()
                qry1 = "select * from data where VACCINATION='{}'".format(va.get())
                cursor.execute(qry1)
                out = cursor.fetchall()
                if not out:
                    messagebox.showwarning('EMPTY', 'NO ANIMAL FOUND WITH VACCINATION STATUS "{}"'.format(va.get()))
                    dell.destroy()
                else:
                    qry = "Delete from data where VACCINATION ='{}'".format(va.get())
                    cursor.execute(qry)
                    mycon.commit()
                    messagebox.showinfo('done', 'deleted!!')
                    dell.destroy()
                
            specbut = Button(dell, text = 'delete', font=('Calibri',10), padx = 5,bg='light blue', command = dil) 
            specbut.pack()
        
        else:
            messagebox.showwarning('ERROR', 'Please choose an option from dropdown menu!!')
            dell.destroy()
            deletee()
    
    submit_button = Button(dell, text='Submit', command=spec_DEL, font = ('Calibri', 15))
    submit_button.pack()
    dell.mainloop()

def log_out():
    login.destroy()
    loogin()


def modify():
        mody = Tk()
        mody.title("MODIFY DATA")
        mody.geometry('1000x400')
        options_list = ["species", "origin", "age", "breed", "vaccination status"]
        value_inside = StringVar(mody)
        value_inside.set("Select an Option")
        question_menu = OptionMenu(mody, value_inside, *options_list)
        question_menu.pack()
        
        def specc():
            if value_inside.get() == "species":
                namee = Label(mody, text = 'Enter the species you want to modify',font=("calibri",25))
                namee.pack()
          
                name = Entry(mody, width=10, fg='blue', font = ('Calibri', 25) )
                name.pack()

                namee2 = Label(mody, text = 'Enter new name for the species', font=("calibri",25))
                namee2.pack()
          
                name2 = Entry(mody, width=10, fg='blue', font = ('Calibri', 25) )
                name2.pack()

                print(name2.get(), name.get())
                def mod_spec():
                    cur = mycon.cursor()
                    
                    qry1 = "select * from data where SPECIES ='{}'".format(name.get())
                    cur.execute(qry1)
                    out = cur.fetchall()

                    if not out:
                        messagebox.showwarning('EMPTY', 'THE SPECIES "{}" DOESNT EXIST'.format(name.get()))
                        mody.destroy()
                    else:
                        qry = "UPDATE data SET SPECIES = '{}' WHERE SPECIES = '{}'".format(name2.get(), name.get())
                        cur.execute(qry)
                        qry2 = "select * from data where SPECIES = '{}'".format(name2.get())
                        cur.execute(qry2)
                        out = cur.fetchall()
                        mycon.commit()
                        mody.destroy()
                        tablee = Tk()
                        i=1
                        for student in out: 
                            for j in range(len(student)):
                                e = Entry(tablee, width=10, fg='blue') 
                                e.grid(row=i, column=j) 
                                e.insert(END, student[j])
                            i=i+1
                        ncci=Label(tablee,text="S.No",width=10,fg='blue')
                        ncci.grid(row=0,column=0)
                        ncci1=Label(tablee,text="Species",width=10,fg='blue')
                        ncci1.grid(row=0,column=1)
                        ncci2=Label(tablee,text="Origin",width=10,fg='blue')
                        ncci2.grid(row=0,column=2)
                        ncci3=Label(tablee,text="Age",width=10,fg='blue')
                        ncci3.grid(row=0,column=3)
                        ncci4=Label(tablee,text="Breed",width=10,fg='blue')
                        ncci4.grid(row=0,column=4)
                        ncci5=Label(tablee,text="Vaccination",width=10,fg='blue')
                        ncci5.grid(row=0,column=5)
                        tablee.mainloop() 
                specbut = Button(mody, text = 'modify', font=('Calibri',10), padx = 5,bg='light blue', command = mod_spec) 
                specbut.pack()

            elif value_inside.get() == "origin":
                originn = Label(mody, text = 'Enter the origin of species you want to modify', font=("calibri",25))
                originn.pack()
          
                origin = Entry(mody, width=10, fg='blue', font = ('Calibri', 25) )
                origin.pack()

                origing2 = Label(mody, text = 'Enter new origin for the species', font=("calibri",25))
                origing2.pack()
          
                origin2 = Entry(mody, width=10, fg='blue', font = ('Calibri', 25) )
                origin2.pack()
              
                def mod_spec():
                    cur = mycon.cursor()
                    qry1 = "select * from data where ORIGIN ='{}'".format(origin.get())
                    cur.execute(qry1)
                    out = cur.fetchall()

                    if not out:
                        messagebox.showwarning('EMPTY', 'THE ORIGIN "{}" DOESNT EXIST'.format(origin.get()))
                        mody.destroy()
                    else:
                        qry = "UPDATE data SET ORIGIN = '{}' WHERE ORIGIN = '{}'".format(origin2.get(), origin.get())
                        cur.execute(qry)
                        qry2 = "select * from data where ORIGIN = '{}'".format(origin2.get())
                        cur.execute(qry2)
                        out = cur.fetchall()
                        mycon.commit()
                        mody.destroy()
                        tablee = Tk()
                        i=1
                        for student in out: 
                            for j in range(len(student)):
                                e = Entry(tablee, width=10, fg='blue') 
                                e.grid(row=i, column=j) 
                                e.insert(END, student[j])
                            i=i+1
                        ncci=Label(tablee,text="S.No",width=10,fg='blue')
                        ncci.grid(row=0,column=0)
                        ncci1=Label(tablee,text="Species",width=10,fg='blue')
                        ncci1.grid(row=0,column=1)
                        ncci2=Label(tablee,text="Origin",width=10,fg='blue')
                        ncci2.grid(row=0,column=2)
                        ncci3=Label(tablee,text="Age",width=10,fg='blue')
                        ncci3.grid(row=0,column=3)
                        ncci4=Label(tablee,text="Breed",width=10,fg='blue')
                        ncci4.grid(row=0,column=4)
                        ncci5=Label(tablee,text="Vaccination",width=10,fg='blue')
                        ncci5.grid(row=0,column=5)
                        tablee.mainloop() 
                specbut = Button(mody, text = 'modify',font=('Calibri',10), padx = 5,bg='light blue',command = mod_spec) 
                specbut.pack()
            
            elif value_inside.get() == "age":
                agee = Label(mody, text = 'Enter the age of species you want to modify', font=("calibri",25))
                agee.pack()
          
                age = Entry(mody, width=10, fg='blue', font = ('Calibri', 25))
                age.pack()

                agee2 = Label(mody, text = 'Enter new age for the species', font=("calibri",25))
                agee2.pack()
          
                age2 = Entry(mody, width=10, fg='blue', font = ('Calibri', 25) )
                age2.pack()
            
                def mod_spec():
                    cur = mycon.cursor()
                    qry1 = "select * from data where AGE ={}".format(age.get())
                    cur.execute(qry1)
                    out = cur.fetchall()

                    if not out:
                        messagebox.showwarning('EMPTY', 'THE AGE {} DOESNT EXIST'.format(age.get()))
                        mody.destroy()
                    else:
                        qry = "UPDATE data SET AGE = {} WHERE AGE = {}".format(age2.get(), age.get())
                        cur.execute(qry)
                        qry2 = "select * from data where age = '{}'".format(age2.get())
                        cur.execute(qry2)
                        out = cur.fetchall()
                        mycon.commit()
                        mody.destroy()
                        tablee = Tk()
                        i=1
                        for student in out: 
                            for j in range(len(student)):
                                e = Entry(tablee, width=10, fg='blue') 
                                e.grid(row=i, column=j) 
                                e.insert(END, student[j])
                            i=i+1
                        ncci=Label(tablee,text="S.No",width=10,fg='blue')
                        ncci.grid(row=0,column=0)
                        ncci1=Label(tablee,text="Species",width=10,fg='blue')
                        ncci1.grid(row=0,column=1)
                        ncci2=Label(tablee,text="Origin",width=10,fg='blue')
                        ncci2.grid(row=0,column=2)
                        ncci3=Label(tablee,text="Age",width=10,fg='blue')
                        ncci3.grid(row=0,column=3)
                        ncci4=Label(tablee,text="Breed",width=10,fg='blue')
                        ncci4.grid(row=0,column=4)
                        ncci5=Label(tablee,text="Vaccination",width=10,fg='blue')
                        ncci5.grid(row=0,column=5)
                        tablee.mainloop() 
                specbut = Button(mody, text = 'modify', font=('Calibri',10), padx = 5,bg='light blue', command = mod_spec) 
                specbut.pack()
        
            elif value_inside.get() == "breed":
                breedd = Label(mody, text = 'Enter the breed you want to modify', font=("calibri",25))
                breedd.pack()
          
                breed = Entry(mody, width=10, fg='blue', font = ('Calibri', 25) )
                breed.pack()

                breedd2 = Label(mody, text = 'Enter new breed for the species', font=("calibri",25))
                breedd2.pack()
          
                breed2 = Entry(mody, width=10, fg='blue', font = ('Calibri', 25) )
                breed2.pack()
            
                def mod_spec():
                    cur = mycon.cursor()
                    qry1 = "select * from data where BREED ='{}'".format(breed.get())
                    cur.execute(qry1)
                    out = cur.fetchall()

                    if not out:
                        messagebox.showwarning('EMPTY', 'THE BREED "{}" DOESNT EXIST'.format(breed.get()))
                        mody.destroy()
                    else:
                        qry = "UPDATE data SET BREED = '{}' WHERE BREED = '{}'".format(breed2.get(), breed.get())
                        cur.execute(qry)
                        qry2 = "select * from data where BREED = '{}'".format(breed2.get())
                        cur.execute(qry2)
                        out = cur.fetchall()
                        mycon.commit()
                        mody.destroy()

                        tablee = Tk()
                        i=1
                        for student in out: 
                            for j in range(len(student)):
                                e = Entry(tablee, width=10, fg='blue') 
                                e.grid(row=i, column=j) 
                                e.insert(END, student[j])
                            i=i+1
                        ncci=Label(tablee,text="S.No",width=10,fg='blue')
                        ncci.grid(row=0,column=0)
                        ncci1=Label(tablee,text="Species",width=10,fg='blue')
                        ncci1.grid(row=0,column=1)
                        ncci2=Label(tablee,text="Origin",width=10,fg='blue')
                        ncci2.grid(row=0,column=2)
                        ncci3=Label(tablee,text="Age",width=10,fg='blue')
                        ncci3.grid(row=0,column=3)
                        ncci4=Label(tablee,text="Breed",width=10,fg='blue')
                        ncci4.grid(row=0,column=4)
                        ncci5=Label(tablee,text="Vaccination",width=10,fg='blue')
                        ncci5.grid(row=0,column=5)
                        tablee.mainloop() 
                specbut = Button(mody, text = 'modify', font=('Calibri',10), padx = 5,bg='light blue', command = mod_spec) 
                specbut.pack()
        
            elif value_inside.get() == "vaccination status":
                vacc = Label(mody, text = 'Enter the species name to modify vaccination status', font=("calibri",25))
                vacc.pack()
          
                vac = Entry(mody, width=10, fg='blue', font = ('Calibri', 25) )
                vac.pack()

                vacc2 = Label(mody, text = 'Enter the vaccination status', font=("calibri",25))
                vacc2.pack()
          
                vac2 = Entry(mody, width=10, fg='blue', font = ('Calibri', 25) )
                vac2.pack()

           
                def mod_spec():
                    cur = mycon.cursor()
                    qry1 = "select * from data where SPECIES ='{}'".format(vac.get())
                    cur.execute(qry1)
                    out = cur.fetchall()

                    if not out:
                        messagebox.showwarning('EMPTY', 'NO ANIMALS EXIST WITH "{}" VACCINATION STATUS DOESNT EXIST'.format(vacc.get()))
                        mody.destroy()
                    else:
                        qry = "UPDATE data SET VACCINATION = '{}' WHERE SPECIES = '{}'".format(vac2.get(), vac.get())
                        cur.execute(qry)
                        qry2 = "select * from data where VACCINATION = '{}' and SPECIES = '{}'".format(vac2.get(), vac.get())
                        cur.execute(qry2)
                        out = cur.fetchall()
                        mycon.commit()
                        mody.destroy()
                        tablee = Tk()
                        i=1
                        for student in out: 
                            for j in range(len(student)):
                                e = Entry(tablee, width=10, fg='blue') 
                                e.grid(row=i, column=j) 
                                e.insert(END, student[j])
                            i=i+1
                        ncci=Label(tablee,text="S.No",width=10,fg='blue')
                        ncci.grid(row=0,column=0)
                        ncci1=Label(tablee,text="Species",width=10,fg='blue')
                        ncci1.grid(row=0,column=1)
                        ncci2=Label(tablee,text="Origin",width=10,fg='blue')
                        ncci2.grid(row=0,column=2)
                        ncci3=Label(tablee,text="Age",width=10,fg='blue')
                        ncci3.grid(row=0,column=3)
                        ncci4=Label(tablee,text="Breed",width=10,fg='blue')
                        ncci4.grid(row=0,column=4)
                        ncci5=Label(tablee,text="Vaccination",width=10,fg='blue')
                        ncci5.grid(row=0,column=5)
                        tablee.mainloop() 
                specbut = Button(mody, text = 'modify', font=('Calibri',10), padx = 5,bg='light blue', command = mod_spec) 
                specbut.pack()
        
            else:
                messagebox.showwarning('error', 'please choose an option from dropdown menu!!')
                mody.destroy()
                modify()

        submit_button = Button(mody, text='Submit', command=specc, font = ('Calibri', 15))
        submit_button.pack()

        mody.mainloop()
    
def loogin():
    global loggin
    loggin=Tk()
    loggin.config(bg='honeydew3')
    
    

    loggin.geometry("850x500")
    loggin.title("LOGIN")

    Name=Label(loggin,text="Wildlife Rescuer",font=("algerian",50,"bold"),fg="black",bg='honeydew3')
    Name.grid(row=0,column=2)

    username=Label(loggin,text="Username:",font=("calibri",25),fg="black",bg='honeydew3')
    username.grid(row=1,column=1)

    password=Label(loggin,text="Password:",font=("calibri",25),fg="black",bg='honeydew3')
    password.grid(row=2,column=1)

    global euname
    euname=Entry(loggin,font=("calibri",25),bd=10)
    euname.grid(row=1,column=2)
 
    global epass
    epass=Entry(loggin,font=("calibri",25),bd=10,show="*")
    epass.grid(row=2,column=2)

    Button1=Button(loggin,text="Create Account",fg="black",font=("calidri",10),bg='light blue',padx=10,pady=10,cursor="hand2",command=Neww)
    Button1.grid(row=6,column=2)

    Button2=Button(loggin,text="Login",fg="black",font=("calidri",10),bg="light blue",padx=40,pady=10,cursor="hand2", command=loginn)
    Button2.grid(row=3,column=2)

    loggin.mainloop()
loogin()
mycon.commit()