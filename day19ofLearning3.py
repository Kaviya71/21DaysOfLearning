print("Temperature converter")
class temperature:
    def __init__(self):
        self.tmp=int(input("Enter the temperature: "))
    def ftoc(self):
        print("Celcius=",(self.tmp-32)*5/9)
    def ctof(self):
        print("Farenhiet=",(self.tmp-9/5)+32)
t=temperature()
print("1.Convert Farenheit to celcius")
print("2.Convert Celcius to Farenheit")
choice=int(input("Entet your choice: "))
if choice==1:
    t.ftoc()
elif choice==2:
    t.ctof()
else:
    print("Invalid choice")
