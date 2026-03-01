employee={
    'Kaviya':70000,
    'Alice':82000,
    'Bob':64000,
    'Carles':58000
}
print(employee)
employee['Jim']=4000
print(employee)
employee['John']=62000
print('The salary management of employee is:',employee)

for name,salary in employee.items():
    if salary>69000:
        print(name,salary)
highest=max(employee,key=employee.get)
print('highest salary: ',highest,employee[highest])
