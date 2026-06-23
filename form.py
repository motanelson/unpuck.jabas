import copy
print("\033c\033[47;31m\ngive me the .form file name to open ? \n ")
a=input().strip()
#a="my.form"
f1=open(a,"r")
b=f1.read()
f1.close()
c=""
f="""
    public static $1 $2($3){
        return $4;
    }
"""
x=[]
l="c"
h="class $1\n{\n"
d=b.split("\n")
count=0
for z in d:
    if count==0:
        a=0
        
    
    if count>0:
        x=z.split("|")
        if count==1:
            
            c=x[0].replace(".java","")
            
            h=h.replace("$1",c)
            
        g=copy.copy(f)
        if len(x)>1:
            g=g.replace("$2",x[1])
            g=g.replace("$1",x[2])
            
            i=int(x[3])
            k="" 
            l="a"
            m=ord(l)
            for j in range(i):
                  if j!=0:
                       k=k+" , "
                  k=k+" "+x[2]+" "+chr(m +j)
            g=g.replace("$3",k)
            g=g.replace("$4",x[4])    
            h=h+g+"\n"   
    count=count+1


print(h+"}")

