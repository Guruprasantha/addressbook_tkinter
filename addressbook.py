from tkinter import*
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector
from mysql.connector import Error

def database():
    global conn, cursor
    conn = mysql.connector.connect( host = "localhost", 
    user = "root",
    passwd = "root",
    database="address_book",
    auth_plugin="mysql_native_password")
    cursor = conn.cursor()



def view():
     database()
     cursor.execute("SELECT * FROM address")
     # Fetch all the rows
     rows = cursor.fetchall()
     # Create a treeview widget to display the data
     tree = ttk.Treeview(main, columns=list(range(len(cursor.column_names))), show="headings")
     # Set the column headings
     for idx, column_name in enumerate(cursor.column_names):
         tree.heading(idx, text=column_name)
         tree.column(idx, width=100)
     for row in rows:
         tree.insert('', 'end', values=row)
     tree.grid(row=12,columnspan=3)
     cursor.close()
     conn.close()
     final1=Label(main,text="the addresses are ..",font=("Comic Sans MS",20,"bold"),bg="steelblue")
     final1.grid(row=10,columnspan=2)

def delete():
    database()
    g1=enter7.get()
    if(g1==""):
        MessageBox.showinfo("INCORRECT SYNATX","enter a valid register number")
    else:
    
        cursor.execute("DELETE FROM address WHERE reg_no = %s", (g1,))
        conn.commit()
        cursor.close()
        conn.close()

        final1=Label(main,text="the address deleted sucessfully",font=("Comic Sans MS",20,"bold"),bg="steelblue")
        final1.grid(row=11,columnspan=2)

def add():
    database()
    a=enter1.get()
    b=enter2.get()
    c=enter3.get()
    d=enter4.get()
    e=enter5.get()
    f=enter6.get()
    g=enter7.get()
    if(a==""or b=="" or c=="" or d=="" or e=="" or f=="" or g=="" ):
        MessageBox.showerror("DATA MISSING","fill all the blocks..")
    else:
        add=("INSERT INTO`address`(reg_no,name_,phone_no,d_no,city,district,pincode)VALUES(%s,%s,%s,%s,%s,%s,%s)")
        data=(g,a,b,c,d,e,f)
        cursor.execute(add,data)
        conn.commit()
        cursor.close()
        conn.close()
        final=Label(main,text="REGISTERED SUCCESSFULLY..",font=("Comic Sans MS",20,"bold"),bg="steelblue")
        final.grid(row=9,columnspan=2)

main=Tk()
main.geometry("1000x700")
main.title("ADDRESS REGISTER")
main.configure(bg="steelblue")
title=Label(main,text="ADDRESS REGISTRATION FORM..",font=("Comic Sans MS",20,"bold"),bg="steelblue")
title.grid(row=0,columnspan=4)

label1=Label(main,text=" NAME :",font=("Copperplate",10,"bold"))
label1.grid(row=1,column=0)
enter1=Entry(main,width=50)
enter1.grid(row=1,column=1)

label2=Label(main,text=" PHONE NO  :",font=("Copperplate",10,"bold"))
label2.grid(row=2,column=0,pady=20)
enter2=Entry(main,width=50)
enter2.grid(row=2,column=1)

address=Label(main,text=" ADDRESS :",font=("Copperplate",18,"bold"))
address.grid(row=3,columnspan=2)

label3=Label(main,text=" D/NO,STREET NAME:",font=("Copperplate",10,"bold"))
label3.grid(row=4,column=0,pady=20,padx=10)
enter3=Entry(main,width=50)
enter3.grid(row=4,column=1)

label4=Label(main,text=" CITY :",font=("Copperplate",10,"bold"))
label4.grid(row=5,column=0)
enter4=Entry(main,width=50)
enter4.grid(row=5,column=1)

label5=Label(main,text=" DISTRICT:",font=("Copperplate",10,"bold"))
label5.grid(row=6,column=0,pady=20)
enter5=Entry(main,width=50)
enter5.grid(row=6,column=1)

label6=Label(main,text=" PINCODE :",font=("Copperplate",10,"bold"))
label6.grid(row=7,column=0)
enter6=Entry(main,width=50)
enter6.grid(row=7,column=1)

label7=Label(main,text="REGISTER NO: ",font=("Copperplate",10,"bold"))
label7.grid(row=8,column=0)
enter7=Entry(main)
enter7.grid(row=8,column=1,pady=20)

button1=Button(main,text="ADD",font=("Copperplate",10,"bold"),command=add)
button1.grid(row=1,column=3,padx=80)

button2=Button(main,text="VIEW TABLE",font=("Copperplate",10,"bold"),command=view)
button2.grid(row=7,column=3,padx=80)

button4=Button(main,text="DELETE",font=("Copperplate",10,"bold"),command=delete)
button4.grid(row=3,column=3,padx=80)

main.mainloop()