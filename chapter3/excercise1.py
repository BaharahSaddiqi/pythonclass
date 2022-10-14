
work_hours=int(input("Enter your working Hours "))
if work_hours>=45:
 work_rate=int(input("Enter your Rate  "))
 pay = work_rate * work_hours* 1.5
 print("your Salary is :", pay)
else:
    print("your input is not on range ") 