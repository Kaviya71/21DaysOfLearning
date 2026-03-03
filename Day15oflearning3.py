print("To reverse a number and count the number of digits in the number")
num=int(input("Enter a number to be reversed: "))
original=num
reversed=0
count=0
while num>0:
    digit=num%10
    reversed=reversed*10+digit
    num=num//10
    count+=1
print("The reversed order of the give number",original,"is",reversed)
print("The number of digits in the given number",original,"is",count)


