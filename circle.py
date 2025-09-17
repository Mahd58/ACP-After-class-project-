class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14159*(self.radius**2)
    def perimeter(self):
        return 2*3.14159*self.radius
r=float(input("Enter the radius of the circle: "))
circle=Circle(r)
print("Area of the circle:",circle.area())
print("Perimeter of the circle:",circle.perimeter())