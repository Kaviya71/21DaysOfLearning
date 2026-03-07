print("This is the calculator using class")
class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("Addtion=",self.num1+self.num2)
    def sub(self):
        print("Subtraction=",self.num1-self.num2)
    def mul(self):
        print("multiplication=",self.num1*self.num2)
    def div(self):
        print("Division=",self.num1/self.num2)
    def pow(self):
        print("Power=",selfnum1**self.num2)

a=calculator(30,5)

print("1.Adiition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Power")
choice=int(input("Enter your choice: "))
      

if choice==1:
    a.add()
elif choice==2:
    a.sub()
elif choice==3:
    a.mul()
elif choice==4:
    a.div()
elif choice==5:
    a.pow()
else:
    print("Invalid choice.Please enter a valid choice")


        
