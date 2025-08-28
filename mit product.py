a=int(input("enter a number: "))
temp=a
numlen=0
while temp>0:
      numlen=numlen+1
      temp=int(temp/10)
if numlen>=4:
      numlen=int(numlen/2)
      chk=0
      while a>0:
            rem=a%10
            if chk==numlen:
                  mid1=rem
            elif chk==(numlen-1):
                  mid2=rem
            a=int(a/10)
            chk=chk+1
      product=mid1*mid2
      print("product of mid digits",product)
else:
      print("it is not more than 4 digits")
        
