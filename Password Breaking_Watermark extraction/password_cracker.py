import hashlib,string
import itertools

alphabet=string.ascii_lowercase
pwdlen=int(input("enter length of password:"))
no_md5s=int(input("enter number of passwords to find:"))
md5s=[]
strinlis={}
for i in range(no_md5s):
    md5s.append(input("enter md5 for password "+str(i+1)+" :"))
i=0
for pwd in itertools.product(alphabet,repeat=pwdlen): 
    pwd_byt_str=''.join(pwd).encode()
    md5hash=hashlib.md5(pwd_byt_str).hexdigest()
    if md5hash in md5s:
        strinlis.update({''.join(pwd):md5hash})
        print("password with md5 "+md5hash+" is : '"+''.join(pwd)+"'")
        i=i+1
    if i==len(md5s):
        break


   
