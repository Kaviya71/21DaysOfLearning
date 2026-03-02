print("To print a reverse number")
num=int(input("Enter a number: "))
original=num
rev=0
while num>0:
   digit=num%10
   rev=rev*10+digit
   num=num//10
print("The reversed number of",original,"is",rev)
    
