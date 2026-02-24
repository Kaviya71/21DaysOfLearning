salary=[]
n=int(input('enter the number: '))
for i in range(n):
    num=int(input("enter the values: "))
    salary.append(num)
print('Salary of the employee: ',salary)
total=0
total=sum(salary)
print('Total salary of the employee: ',total)
highest=salary[0]
lowest=salary[0]
for num in salary:
    if num > highest:
        highest=num
    elif num < lowest:
        lowest=num

print('Highest amount: ',highest)
print('Lowest amount: ',lowest)
count=0
for num in salary:
    if num>5000:
        count=+1
print("The earning of the employee above 5000 is :",count)
            
        
    
   
