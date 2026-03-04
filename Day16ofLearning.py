while True:
    print("Menu driven number system")
    print("1.Reverse a number")
    print("2.Sum of the digits in a number")
    print("3.Count the number of digits in a number")
    print("4.Check prime number")
    print("5.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        n=int(input("Enter the number to reverse: "))
        rev=0
        while n>0:
            digit=n%10
            rev=rev*10+digit
            n=n//10
        print("The reversed number is",rev)
    elif choice==2:
        n=int(input("Enter the number to find the sum of digits: "))
        sum=0
        while n>0:
            digit=n%10
            sum+=digit
            n=n//10
        print("The sum of the digits of a number is",sum)
    elif choice==3:
        n=int(input("Enter the number to count the number of digits: "))
        count=0
        while n>0:
            n=n//10
            count+=1
        print("The count of number of digits in a number is",count)
    elif choice==4:
        n=int(input("Enter the number to check prime: "))
        if n<=1:
            print("The number",n,"is not prime")
        else:
            for i in range(2,n):
                if n%i==0:
                    print("not prime")
                    break
                else:
                    print("prime")
    elif choice==5:
        print("Exiting program")
        break
    else:
        print("Invalid choice")
        
            
            
               
        
