medical=input("do you have a medical condition Y or N")
att=int(input("enter your attendence: "))
if medical=='Y':
    print("you are allowed")
else:
     if att>=75:
       print("you are allowed")
     else:
          print("you are not allowed")