print("To find the LCM and HCF of two numbers")
a=int(input("enter the num 1: "))
b=int(input("Enter the num 2: "))
hcf=1
lcm=1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        hcf=i
    lcm=(a*b)//hcf
print("The hcf of the numbers",a,"and",b,"is",hcf)
print("The lcm of the numbers",a,"and",b,"is",lcm)
