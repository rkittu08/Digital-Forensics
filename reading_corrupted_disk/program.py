import base64
import binascii
import hashlib

filename=input("Enter file name along with path:")
out_file=input("Enter out file path:")
#filename='/Volumes/Ram/Study/Fall/Digital Forensics/Assignment 1/corrupted.docx'
k=''
f= open(filename,'r')

for line in f:
    
    if line != '':
        k=k+line
a=base64.b64decode(k) #decoding b64 into byte data
f.close()

b=binascii.b2a_hex(bytearray(a)) # Hex conversion

b=str(b)
b=b[2:len(b)-1]


typ=input("Enter JPG or PDF or PNG or GIF or DOCX or None to exit :")
while(typ != "None" ):
    output_file=out_file+typ+'extract.'+typ
    hd=input("Header for given file type:")
    ft=input("Footer for given file type:")
    out_content=b[b.index(hd):][:b[b.index(hd):].index(ft)+len(ft)]
    g=open(output_file,'wb')
    byte_string=binascii.unhexlify(out_content)
    md5hash=hashlib.md5(byte_string).hexdigest()
    g.write(byte_string)
    print("MD5 for "+typ+":"+md5hash)
    print(output_file+" is created")
    g.close()
    typ=input("Enter JPG or PDF or PNG or GIF or DOCX or None :")

print("Good Bye")
    







    

