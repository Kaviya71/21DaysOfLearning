class students:
    def get_data(self):
        self.name=input("Enter the name: ")
        self.rollno=int(input("enter the roll number of the student: "))
        self.marks=int(input("Enter the mark of the student: "))
    def display(self):
        print("The name of the student is",self.name)
        print("The roll number of the student is",self.rollno)
        print("The marks obtained by the student is",self.marks)
while True:
    s1=students()
    s1.get_data()
    s1.display()
        
        
