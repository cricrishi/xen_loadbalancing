import os
import sys
import time



l=[0]*3
def fileread():
    with open('rishi23.txt', 'r') as f:
        for line in f:
            a = line
            array.append((a))
        words2=array[6].split()
        for word in words2:
            c=words2
        words3=array[7].split()
        for word in words3:
            d=words3
        l[1]=float(c[3])/float(c[8])
        l[2]=float(d[3])/float(d[8])    
         
    
def rralgo(l,s):
    #print l[0],l[1],l[2]
    k=l[0]
    k=k+1
    c=1;
    while(l[0]<(s-1)):
        fileread()
        if(l[k]<threshold):
            print"assigning application to virtual machine-->  ",k

	    f1="vm"
	    f1=f1+str(k)
	    str1=".sh"
	    f1=f1+str1
	    
	    f = open(f1,"w")
	    f.truncate()
	    if(file_name=="summer.docx"):
		f.write("libreoffice ")
	    elif(file_name=="news.txt"):
		f.write("gedit ")
	    else:
		f.write("")
	    
            f.write(file_name)
            f.close() 
            print "Toatal no of VM check", c
            print "  "
            
            if(k==(s-1)):
                k=0
            l[0]=k    
            break
            
        else:
            print("virtual machine",k,"is overloaded")
            print("checking next virtual machine")
            print ""
            #print k,s
            c=c+1
            if(k ==(s-1)):
                
                k=1
            else:
                
                k=k+1
            
               
#os.system('xentop -i2 -b > rishi23.txt')

array=[]

with open('rishi23.txt', 'r') as f:
    for line in f:
        a = line
        
        array.append((a))

words=array[4].split()
for word in words:
    a=words


words1=array[5].split()
for word in words1:
    b=words1


words2=array[6].split()
for word in words2:
    c=words2

words3=array[7].split()
for word in words3:
    d=words3
for i in range(0,19):
    print a[i], b[i], c[i], d[i]

fileread()

l[0]=0;
l[1]=float(c[3])/float(c[8])
l[2]=float(d[3])/float(d[8])
#l[3]=47

print int(l[1])
print int(l[2])

print("which application u want to open in virtual machines")
print("Available applications are give n below")
os.system('ls')


threshold=80;


print("evaluting load on virtual machines")
time.sleep(1)
print("load on virtual machine1")
print l[1]

print ("load on virtual machine2")
s1=len(l)
print l[2]
z="y"
while(z=='y'):
    print("which application u want to open in virtual machines")
    print("Available applications are give n below")
    os.system('ls')
    print("enter the filename that u want to open")
    file_name=raw_input()
    rralgo(l,s1)
    print "open more application enter y"
    z=raw_input()














    
