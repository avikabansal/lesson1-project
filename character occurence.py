word1=input("enter a word: ")
character=input("enter the character ")
i=0
count=0
while(i<len(word1)):
    if(word1[i]==character):
     count =count+1
    i=i+1
print("the number of times",character,"has occur",count)
