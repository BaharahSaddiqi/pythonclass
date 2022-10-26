def grad_student(score):

 if score>=0.0 and score<=1.0:
  if score>=0.9:
     return"A"
  elif score>=0.8:
     return "B"
  elif score>=0.7:
     return "C"
  elif score>=0.6:
     return "D"      
  elif score<0.6:
     return "F"
 else :
    return"please inter in ringe from 0,0 to 1,0 "




  
input_score = input("Enter score: ") 
score=0.0

try:
    score = float(input_score)             
except ValueError:
    print("bad score")
    quit()

grade = grad_student(score)
print(grade)