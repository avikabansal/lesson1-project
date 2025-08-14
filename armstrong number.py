num1=int(input("enter a number: "))
sum=0
temp=num1
while  temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num1==sum:
             print(num1,"is an armstrong number")
else:
     print(num1,"is not an armstrong number")