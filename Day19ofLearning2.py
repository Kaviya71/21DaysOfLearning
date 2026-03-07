class num_operation:
    def __init__(self,a):
        self.num1=a
    def EvenorOdd(self):
        if self.num1%2==0:
            print("Even")
        else:
            print("odd")
    def square(self):
        print("Square of the number: ",self.num1**2)
    def cube(self):
        print("Cube of the number: ",self.num1**3)
c=num_operation(2)
print("1.Find the number is even or odd")
print("2.Find the square of a number")
print("3.Find the cube of a number")
choice=int(input("Enter you choice: "))
if choice==1:
    c.EvenorOdd()
elif choice==2:
    c.square()
elif choice==3:
    c.cube()
else:
    print("Invalid choice")
        
        
    
        
