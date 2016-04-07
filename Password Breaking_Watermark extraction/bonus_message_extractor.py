import Image

def binarybuild(im,band):
    width,height=im.size
    im.load()
    k=''
    for m in range(0, height):
        for n in range(0, width):
            red, green, blue = im.getpixel((n, m))
            if band=='red':
                 lsb = red%2
            elif band=='green':
                 lsb = green%2
            elif band=='blue':
                 lsb = blue%2
            k = k  + str(lsb)
    return k
im1=Image.open(input("Enter Image1 Path:"))
# "/Users/RamSakhamuri/Desktop/Cchapel/mountain.png"
im2=Image.open(input("Enter Image2 Path:"))
band=input("enter which band to check:")
string1=binarybuild(im1,band)
string2=binarybuild(im2,band)
if string1==string2:
    print(band+" band is same in both images")
else:
    l=0
    string=''
    while (l<len(string2)):
        string+=chr(int(string2[l:l+8],2))
        l+=8
    file1=open(input("Enter Output Path:"),'w')
    print("Find the file with message")
    # "/Users/RamSakhamuri/Desktop/"
    file1.write(string)
    file1.close
