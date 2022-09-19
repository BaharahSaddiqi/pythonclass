 
#this program give mood for number 7 but not number 5
def mood_numbers(number):
    while number<=1300:
        if number %7==0:
            if number %5!=0:
                print(number, "--",end ="")    
        number +=1


mood_numbers(1000)





















