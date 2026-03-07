class interest:
    def __init__(self):
        self.p=int(input("Enter the principle amount: "))
        self.r=int(input("enter the rate of interest: "))
        self.t=int(input("Enter the time period in years: "))
    def SI(self):
        print("The simple interest if calculated to be: ",(self.p*self.r*self.t)/100)
    def amount(self):
        print("The total amount is calculated to be: ",((self.p*self.r*self.t)/100)+self.p)
si1=interest()
print("1.calculate the simple interest")
print("2.Calculate the total amount")
choice=int(input("Enter your choice: "))
if choice==1:
    si1.SI()
elif choice==2:
    si1.amount()
else:
    print("Invlaid choice")
