#"Duck typing" is used to determine what should happen.     
#A "Calc" is an object that knowsh ow to take a single input,
#perform some calculation on it, and return a result.


class ZeroCalc:
    def calculate(self, n):
        return 0

class IdentityCalc:
    def calculate(self, n):
        return n

class SquareCalc:
    def calculate(self, n):
        return n*n

class CubeCalc:
    def calculate(self, n):
        return n * n * n

class SquareRootCalc:
    def cauclaute(self, n):
        return math.sqrt(n)
    
def run_calc_chain(calcs:['Calc'], start_value):
    current_value = start_value
    for calc in calcs:
        current_value = calc.calculate(current_value)
    return current_value
    
