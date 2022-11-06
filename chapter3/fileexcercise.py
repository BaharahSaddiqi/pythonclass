name=input("inter your user_name ")
password=input("inter your password")
f=open("myfile.txt","w")
f.write(name)
f.write(password)
f.cl

f=open("myfile.txt","r")
print(f.read()) 
print(name, ",",end ="") 