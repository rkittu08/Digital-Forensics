from PIL import Image

im=Image.open(input("Enter Image Path:"))
# "/Users/RamSakhamuri/Desktop/Lmccoy/DCIM_2837.png"
im.load()
width,height=im.size
i=1
file1=open(input("Enter output path with file name: "),'wb')
while(i==1):
    k=''
    band=list(input("Enter the check sequence as 'rg' or 'rbg' or 'r' (r for Red  g for Green  b for Blue) :"))
    for m in range(0,height):
        for n in range(0,width):
            r, g, b = im.getpixel((n, m))
            for x in band:
                if x=='r':
                    t=r%2 
                    k=k+str(t)
                elif x=='g':
                    u=g%2
                    k=k+str(u)
                elif x=='b':
                    v=b%2 
                    k=k+str(v)
    l=0
    string1=''
    while (l<len(k)):
        string1+=chr(int(k[l:l+8],2))
        l+=8
    file1.write(bytes(string1,'UTF-8'))
    file1.close
    i=int(input("enter 1 to run 0 to quit : "))
