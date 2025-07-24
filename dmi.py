height=int(input("enter your height: "))
weight=int(input("enter your weight: "))
bmi=weight/(height/100)**2
print("your bmi is",bmi)
if bmi<=19:
    print("you are underweight")
elif bmi<=25:
    print("you are healthy")
elif bmi<=30:
     print("you are overweight")
else:
    print("you are obese")   
