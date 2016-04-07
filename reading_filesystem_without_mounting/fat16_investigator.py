import binascii
## Below function helps to convert a little endian hex string to decimal value
def le_2_de(a):
    l=''
    k=0
    for i in range(0,len(a)/2):
        k=len(a)-2*i
        l=l+a[k-2:k]
    l=int(l,16)
    return l
### Below function is to pull the hex value from hex data of image and print output
def content_pull(a,b):
    l=int(a,16)*2
    data=le_2_de((content[l:l+2*b])) ### here user defined function le_2_de is used to find decimal for little_endian
    return data
### Main program starts here
## /Volumes/Ram/Study/Fall/Digital Forensics/Assignment 3
filename =input("Enter Image file path : ")
f= open(filename,'rb')
content = f.read()
content=binascii.hexlify(content)
f.close()
content_end_byte=len(content)/2
## Created a dictionary boot_dict which stores all the required offsets and lengths
boot_dict={'BPS_O':'000B','BPS_S':2,'SPC_O':'000D','SPC_S':1,'RS_O':'000E','RS_S':2,'NOFC_O':'0010','NOFC_S':1,'NORE_O':'0011','NORE_S':2,'SPF_O':'0016','SPF_S':2}

BPS=content_pull(boot_dict['BPS_O'],boot_dict['BPS_S']) 
RS=content_pull(boot_dict['RS_O'],boot_dict['RS_S'])
SPC=content_pull(boot_dict['SPC_O'],boot_dict['SPC_S']) 
NOFC=content_pull(boot_dict['NOFC_O'],boot_dict['NOFC_S'])
NORE=content_pull(boot_dict['NORE_O'],boot_dict['NORE_S'])
SPF=content_pull(boot_dict['SPF_O'],boot_dict['SPF_S'])
print("Bytes occupied by Boot Block :"+str(BPS)+"\n Bytes per Sector: "+str(BPS)+" \n Reserved Sectors :"+str(RS)+" \n Sectors per Cluster :"
      +str(SPC)+" \n No of FAT copies :"+str(NOFC)+" \n No of Root entries :"+str(NORE)+"\n Sectors per FAT :"+str(SPF))
BOFFAT=RS*BPS
BOSFAT=BOFFAT+SPF*BPS
BOFRDE=BOFFAT+(NOFC*SPF*BPS)
BOFDTB=BOFRDE+NORE*32
NODBB=content_end_byte-BOFDTB
print("Byte Ofset 1st FAT :"+str(BOFFAT)+"\n Byte Ofset of 2nd FAT :"+str(BOSFAT)+"\n Byte Ofset of 1st Root directory Entry :"+str(BOFRDE)+
      "\n Byte Ofset of 1st Data Block :"+str(BOFDTB)+"\n Number of Bytes in Data Block: "+str(NODBB))
