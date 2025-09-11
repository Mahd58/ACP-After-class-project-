class Vehicle():
    def __init__(self,fee):
        self.fee=fee
class Bus(Vehicle):
    def __init__(self, fee):
        super().__init__(fee)
        self.fee=500
        self.fee=fee
total=Bus(500)
print("The price of one travel is",total.fee)
print("remember that you can only travel to 5 places")
user=int(input("Enter how many places do you want to go:"))
if user==1:
    print("total fee will be",total.fee)
if user==2:
    print("total fee will be",total.fee*2)
if user==3:
    print("total fee will be",total.fee*3)
if user==4:
    print("total fee will be",total.fee*4)
if user==5:
    print("total fee will be",total.fee*5)
if user>5:
    print("GET OUT OF MY BUS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")