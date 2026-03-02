print("To find whether the given number is palandrome or not")
num=int(input("Enter a number: "))
original=num
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if original==reverse:
    print("The given number",original,"is a palandrome number")
else:
    print("The given number",original,"is not a palandrome number")
