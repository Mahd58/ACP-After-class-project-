class numbers():
    def input(self,input):
        self.input1=input
class rooman_numbers():
    def __init__(self):
        self.roman_dict={
            1:"I",
            2:"II",
            3:"III",
            4:"IV",
            5:"V",
            6:"VI",
            7:"VII",
            8:"VIII",
            9:"IX",
            10:"X"
        }
    def convert(self,nnumber):
        return self.roman_dict.get(nnumber,"Invalid")
num=int(input("Enter a number(1-10):"))
roman=rooman_numbers()
print("The Roman numeral of this number is =",roman.convert(num))