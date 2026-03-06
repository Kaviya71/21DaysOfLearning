class rectangle:
    def get_data(self):
        self.length=int(input("Enter the length: "))
        self.width=int(input("Enter the width: "))
    def area(self):
        self.area=self.length*self.width
    def perimeter(self):
        self.perimeter=2*(self.length+self.width)
    def display(self):
        print("The area of the rectangle is",self.area)
        print("The perimeter of the rectangle is",self.perimeter)
while True:
    r1=rectangle()
    r1.get_data()
    r1.area()
    r1.perimeter()
    r1.display()
