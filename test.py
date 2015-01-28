s=raw_input()
f = open("vm1.sh","w")
f.truncate()
f.write("libreoffice ")
f.write(s)

f.close() 

