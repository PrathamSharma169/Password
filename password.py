import random as r
import string as s
import time
import tkinter as tk
def check():
    q= entry_1.get()
    count=0
    p=0
    t=0
    l=['1','2','3','4','5','6','7','8','9','0']
    for i in range(len(q)):
        if q[i] in s.ascii_uppercase:
            count=count+1
        if q[i] in s.ascii_lowercase:
            p=p+1
        if q[i] in l:
            t=t+1
    if  count==0:
        print("password must contain one capital letter")
    elif count>1 :
        print("password must contain only one capital letter ")
    elif p>6 :
        print("password must contain only 6 small letters")
    elif p<6 :
        print("password must contain 6 small letters")
    elif t==0 :
        print("password must contain a number")
    elif t>1 :
        print("password must contain only one number")
    elif len(q)>8 or len(q)<8:
        print("password must contain only 8 elements")
def confirm():
    d=entry_2.get()
    q=entry_1.get()
    if d!=q:
        print("wrong password")
    else:
        print("password set succesfully now login")
def login():
    k=entry_3.get()
    q=entry_1.get()
    if(k!=q):
        print("password is incorrect try again later")
    else:
        print("you are loginned succesfully")
m= tk.Tk( className='password')
#q=r.sample(s.ascii_letters,4)
#y=''.join(r.sample(s.printable,4))
#print(y)
tk.Label(m, text="NOTE- your password must contain only 8 digits in which 1 character should be capital , 6 character should be small and 1 character should be a number").grid()
tk.Label(m, text='enter your password').grid()
entry_1 = tk.Entry(m)
entry_1.grid()
button1 = tk.Button(m, text='Set Password', width=25, command=check)
button1.grid()
tk.Label(m, text='confirm password').grid()
entry_2 = tk.Entry(m)
entry_2.grid()
button2 = tk.Button(m, text='confirm', width=25, command=confirm)
button2.grid()


s=tk.Tk(className='login page')
tk.Label(s, text='enter your password').grid()
entry_3 = tk.Entry(s)
entry_3.grid()
button3 = tk.Button(s, text='login', width=25, command=login)
button3.grid()

m.mainloop()
s.mainloop()