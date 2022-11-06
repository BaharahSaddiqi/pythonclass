#i=1
#while i<=5:
  #  print("*" * i)
  #  i=i+1

#------------------------
secret_number=9
guss_count=0
guss_limit=3
while guss_count < guss_limit:
    guss=int (input("Guss: "))
    guss_count+=1

    if guss==secret_number:
     print("you won! :) ")
     break
else:
    print("you faild :(")

