print("To check whether the given number is Armstrong number or not")
num=int(input("Enter a number: "))
original=num
sum=0
digits=len(str(num))
while num>0:
    digit=num%10
    sum=sum+digit**digits
    num=num//10
if original==sum:
    print("The given number",original,"is a Armstrong number")
else:
    print("The given number",original,"is not a Armstrong number")
