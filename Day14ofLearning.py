print("Factorial of a number")
fact=1
num=int(input("Enter a number: "))
if num<0:
    print("The factorial of of negative numbers does not exist")
else:
    for i in range(1,num+1):
        fact=fact*i
print("Factorail of",num,"is",fact)
    
