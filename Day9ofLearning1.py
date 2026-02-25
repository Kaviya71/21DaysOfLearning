print("Bank Management System")
amount=[]
n=int(input("Enter the value "))
for i in range(n):
    salary=int(input("Enter the amount: "))
    amount.append(salary)
print(amount)
while True:
    print("Bank Management System")
    print('1.Check balance')
    print('2.Deposit Money')
    print('3.Withdraw Money')
    print('4.Exit')
    choice=int(input("Enter your choice: "))
    if choice==1:
        print('1.Check balance')
        print("The balance available in your account: ",sum(amount))
    elif choice==2:
        print('2.Deposit Money')
        new_amount=int(input("Enter the amount to deposite in your account: "))
        amount.append(new_amount)
        print(sum(amount))
    elif choice==3:
        print('3.Withdraw Money')
        withdraw_amount=int(input("Enter the amount to withdraw: "))
        if sum(amount)>=withdraw_amount:
            amount.append(-withdraw_amount)
            print("The amount is withdrawn successfully")
            print("The remaing amount in your account is: ",sum(amount))
        else:
            print("There is no sufficient balance in your account to withdraw")
    elif choice==4:
        break
    else:
        print("Invalid input,please enter a valid input to continue")



    
        
           
