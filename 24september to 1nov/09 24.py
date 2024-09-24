class Calculkator:
    def __init__ (self, add = None, subtract = None, multiply = None, divide=None):
        self.add = add
        self.subtract = subtract
        self.multiply = multiply
        self.divide = divide

class CalculationApp:
    def calcul(self):
        while True:
            first_number = int(input("Write your first number:"))
            second_number = int(input ("Write your second number:"))

            calchose = input("Which calculation would you like to do? (add, subtract, multiply, divide)")

            if calchose == "add":
                print(first_number + second_number )
            elif calchose == "subtract":
                print(first_number - second_number)
            elif calchose == "multiply":
                print(first_number * second_number)
            elif calchose == "divide":
                print(first_number / second_number)
            else:
                print("Invalid operation choice!")

app = CalculationApp()
app.calcul()