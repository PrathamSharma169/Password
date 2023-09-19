import random as r
import string as s
import time
#q=r.sample(s.ascii_letters,4)
#y=''.join(r.sample(s.printable,4))
#print(y)
print("NOTE- your password must contain only 8 digits in which 1 character should be capital , 6 character should be small and 1 character should be a number")
q=str(input('enter your password \n'))
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
else:
     d=str(input("confirm password \n"))
     if d!=q:
         print("wrong password")
     else:
         print("password set succesfully now login")
         k=str(input("enter password \n"))
         if(k!=q):
             print("password is incorrect try again later")
         else:
             print("you are loginned succesfully")
    
 
        





