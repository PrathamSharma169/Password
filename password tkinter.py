import random as r
import string as st
import time
import tkinter as tk
def clear_text1():
    label1.config(text=" ")
def clear_text9():
    label9.config(text=" ")
def clear_text11():
    label11.config(text=" ")
def check():
    q= entry_1.get()
    count=0
    p=0
    t=0
    l=['1','2','3','4','5','6','7','8','9','0']
    for i in range(len(q)):
        if q[i] in st.ascii_uppercase:
            count=count+1
        if q[i] in st.ascii_lowercase:
            p=p+1
        if q[i] in l:
            t=t+1
    if  count==0:
        label1.config(text="password must contain one capital letter")
        m.after(3000, clear_text1)
    elif count>1 :
        label1.config(text="password must contain only one capital letter ")
        m.after(3000, clear_text1)
    elif p>6 :
        label1.config(text="password must contain only 6 small letters")
        m.after(3000, clear_text1)
    elif p<6 :
        label1.config(text="password must contain 6 small letters")
        m.after(3000, clear_text1)
    elif t==0 :
        label1.config(text="password must contain a number")
        m.after(3000, clear_text1)
    elif t>1 :
        label1.config(text="password must contain only one number")
        m.after(3000, clear_text1)
    elif len(q)>8 or len(q)<8:
        label1.config(text="password must contain only 8 elements")
        m.after(3000, clear_text1)
    else:
        label1.config(text="now confirm password")
        m.after(3000, clear_text1)
def confirm():
    d=entry_2.get()
    q=entry_1.get()
    if d!=q:
        label9.config(text="wrong password")
        m.after(3000, clear_text9)
    else:
        label9.config(text="password set succesfully now login")
        m.after(3000, clear_text9)
def login():
    k=entry_3.get()
    q=entry_1.get()
    if(k!=q):
        label11.config(text="password is incorrect try again later")
        s.after(3000, clear_text11)
    else:
        label11.config(text="you are loginned succesfully")
        s.after(3000, clear_text11)
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
label1= tk.Label(m,text=' ')
label1.grid()
tk.Label(m, text='confirm password').grid()
entry_2 = tk.Entry(m)
entry_2.grid()
button2 = tk.Button(m, text='confirm', width=25, command=confirm)
button2.grid()
label9= tk.Label(m,text=' ')
label9.grid()


s=tk.Tk(className='login page')
tk.Label(s, text='enter your password').grid()
entry_3 = tk.Entry(s)
entry_3.grid()
button3 = tk.Button(s, text='login', width=25, command=login)
button3.grid()
label11= tk.Label(s,text=' ')
label11.grid()

m.mainloop()
s.mainloop()