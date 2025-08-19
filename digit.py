num=int(input("enter a number: "))
temp=num
counter=0
while num!=0:
    num=num//10
    counter+=1
print("the number",temp,"has",counter,"digits")