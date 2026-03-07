class student:
    college="Sathyabama"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def setmarks(self,name,marks):
        self.name=name
        self.marks=marks
    def getmarks(self):
        print("The name of the student is",self.name)
        print("The marks obtained by the student is",self.marks)
    @classmethod
    def change_college(cls):
        cls.college="Jeppiar college"
        print("The changed college is",cls.college)
    @staticmethod
    def info():
        print("This is the student class")

s1=student("Kaviya",67)
s1.setmarks("Kavzz",90)
s1.getmarks()
s1.change_college()
s1.info()
s2=student("Kavisha",97)
s2.getmarks()
s2.change_college()
s2.info()
        
        
    
