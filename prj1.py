import os
import sys
import time

        
def rralgo(l,s):
    print l[0],l[1],l[2]
    k=l[0]
    k=k+1
    while(l[0]<(s-1)):
        
        if(l[k]<threshold):
            print"assigning application to virtual machine-->  ",k
            l[0]=k
            break
            
        else:
            print("virtual machine",k,"is overloaded")
            print("checking next virtual machine")
            print k,s
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
l=[0]*3
l[0]=0;
l[1]=float(c[3])/float(c[8])
l[2]=float(d[3])/float(d[8])

print int(l[1])
print int(l[2])

print("which application u want to open in virtual machines")
print("Available applications are give n below")
os.system('ls')

print("enter the filename that u want to open")
threshold=80;
#file_name=raw_input()

print("evaluting load on virtual machines")

print("load on virtual machine1")
print l[1]
time.sleep(1)
print ("load on virtual machine2")
s1=len(l)
print l[2]
print l
rralgo(l,s1)
print l
rralgo(l,s1)
rralgo(l,s1)













    
