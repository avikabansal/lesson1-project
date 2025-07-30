print("enter marks obtained in 5 subjects")
maths=int(input())
science=int(input())
french=int(input())
hindi=int(input())
sst=int(input())
total=maths+science+sst+french+hindi
average=total/5
if average>=91 and average<=100:
   print("your grade is A1")
elif average>=81 and average<91:
     print("your grade is A2")
elif average>=71 and average<81:
    print("your grade is B1")
elif average>=61 and average<71:
     print("your age is B2 ")
elif average>=51 and average<61:
     print("your grade is C1")
elif average>=41 and average<51:
     print("your grade is C2")
elif average>=31 and average<41:
     print("your grade is D1")
elif average>=21 and average<31:
     print("your grade is D2")
elif average>=11 and average<21:
     print("your grade is E1")
elif average>=1 and average<11:
     print("your grade is E2")
else:
     print(" it is an invalid input")
     



