class BMW():
    def max_speed(self):
        return "I go 400 KM/H"
class ferrari():
    def max_speed(self):
        return "I go 500 KM/H"
for car in [BMW(),ferrari()]:
    print(car.max_speed())