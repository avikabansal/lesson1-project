print("select your ride")
print("1.bike")
print("2.car")
choice= int(input("enter your choice: "))
if(choice==1):
    print("what type of bike")
    print("1.scooty")
    print("2.scooter")
    choice1=int(input("enter your choice"))
    if (choice1==1):
        print("you chose scooty")
    else:
        print("you chose scooter")
elif(choice==2):
       print("what type of car")
       print("1.SUV")
       print("2.sedan")
       choice2=int(input("enter your choice"))
       if (choice2==1):
        print("you chose SUV")
       else:
        print("you chose sedan")