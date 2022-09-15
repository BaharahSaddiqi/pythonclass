#given input from user 
interList=input("inter your list item:")
#split it in list and split with comma
userlist=interList.split(',')
#print our list
print("your list:", userlist)
#we need a for to convert each iteam from string to integer
for a in range(len(userlist)):
    userlist[a] = int(userlist[a])


