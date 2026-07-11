import os
import copy
print("\033c\033[47;30m\ngive me the .packs pack file ? \n")
a=input().strip()
f1=open(a,"rb")
f=f1.read()
f1.close()
ff=f.split(b"\x01\x00\x05\x04\x03\x07")


ff1=ff[1].split(b"\x01\x00\x05\x04\x03\x02")
if len(ff1)< 2:
    
    if ff1[1]!="JABA":
        printf("this is not a pack file to 1 file")
        exit(1)
names=ff1[1].decode()

try:
    os.mkdir(names,777)
except:
    pass
os.system("chmod 777 "+names)

counter=0
for d in ff:
    if  counter>1 and d.strip()!="":
        ff1=d.split(b"\x01\x00\x05\x04\x03\x02")
        ff1[0]=ff1[0].decode()  
        f1=open(names+"/"+ff1[0],"bw")
        f1.write(ff1[1])
        f1.close()
    counter=counter+1

counter=0