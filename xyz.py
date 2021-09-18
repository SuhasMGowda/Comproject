from tkinter import *
from tkinter import ttk
converter = Tk()
converter.geometry("700x275")
converter.title("Headache")
OPTIONS = {
    "UAE (UAE Dirhams)":20.11,
    "United States (US Dollars)":74.01,
    "Europe (Euros)":90.41,
    "United Kingdom  (Pound Sterlings)":98.59,
    "Canada  (Can Dollars)":57.57,
    "Australia  (Australian Dollars)":55.64,
    "Switzerland  (Swiss Francs)":69.62,
    "Denmark (Danish Krone)":12.15,
    "Norway  (Norwegian Krones)":8.53,
    "Sweden  (Swedish Kronas)":8.94,
    "Hong Kong  (HK Dollars)":9.51,
    "Egypt (Egyptian Pound)":4.72,
    "Japan (Yenes)":0.71,
    "Russia( Ruble)":0.98,
    "Indonesia (Rupiahs)":0.005,
    "Singapore (Singapore Dollars)":1,
    "South Korean (South Korean Wons)":0.069,
    "South Africa (South African Rand)":4.99,
    "China (Yuan)":11.26,
    "India  (Indian Rupees)":1,
    "Pakistan (rupee)":0.459,
    "Sri Lanka (rupee)":0.39,
    "Mexico (Mexican Peso)":3.67,
    "Brazil (Brazilian Real)":14.388
    }
def ok():
    price = rupees.get()
    answer  = variable.get()
    DICT = OPTIONS.get(answer,None)
    converted = float(price)/float(DICT)
    result.delete(1.0,END)
    result.insert(INSERT,"Price In: ",INSERT,answer,INSERT," = ",
                  INSERT,converted)
appName = Label(converter,text="Currency",
                font=("algerian",25,"bold"),fg="dark blue")
appName.grid(row=0,column=0,padx=10)

appName = Label(converter,text="Convertor",
                font=("algerian",25,"bold"),fg="dark blue")
appName.grid(row=0,column=2,ipadx=10)

result= Text(converter,height=5,width=50,font=("arial",10),bd=5)
result.grid(row=5,columnspan=10,padx=3)
india = Label(converter,text="Choose Country:",
              font=("Chiller",20,"bold"),fg="red")
india.grid(row=3,column=0)
rupees = Entry(converter,font=("calibri",20))
rupees.grid(row=2,column=1)
choice = Label(converter,text="Indian Rupees:",
              font=("Chiller",20,"bold"),fg="red")
choice.grid(row=2,column=0)
variable = StringVar(converter)
variable.set(None)
option = OptionMenu(converter,variable,*OPTIONS)
option.grid(row=3,column=1,sticky="ew")
button = Button(converter,text="Convert",fg="yellow",
                font=("Ink Free",20,"bold"),bg="red",command=ok)
button.grid(row=3,column=2)
mainloop()
#this is a change
