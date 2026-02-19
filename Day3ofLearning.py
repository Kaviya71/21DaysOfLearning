a=int(input('enter a number1:'))
b=int(input('enter a number2:'))
print('Choose any one of the following options to perform calculation')
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')
print('5.Exponential')
n=int(input("Enter your choice"))
match n:
    case 1:
        if n==1:
            print(a+b)
        
    case 2:
        if n==2:
            print(a-b)
        
    case 3:
        if n==3:
            print(a*b)
        
    case 4:
        if n==4:
            print(a%b)
        
    case 5:
        if n==5:
            print(a**b)

    case _:
        print("Invalid number")
        


        
        
            
    
      
    
