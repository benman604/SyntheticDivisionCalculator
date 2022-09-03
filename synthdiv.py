from tabulate import tabulate
import copy
class SynthDiv:
    def __init__(self, coef, zero):
        self.coef = coef
        self.zero = zero
        self.row3 = [0] * len(coef)
        self.row2 = [0] * len(coef)

    # computes synthetic division column by column
    def calc(self):
        self.row3[0] = self.coef[0]
        for i in range(len(self.coef)-1):
            self.row2[i+1] = self.row3[i] * self.zero
            self.row3[i+1] = self.coef[i+1] + self.row2[i+1]
        return self.row3

    # displays table of values
    def disp(self):
        row1 = copy.copy(self.coef)
        row2 = copy.copy(self.row2)
        row3 = copy.copy(self.row3)
        row1.insert(0, self.zero)
        row2[0] = " "
        row2.insert(0, " ")
        row3.insert(0, " ")
        print(tabulate([row1, row2, row3]))
        print()
     
    # displays division quotient
    def dispQuotient(self):
        values = self.calc()
        quotient = ""
        for i in range(len(values) - 2):
            quotient += str(values[i]) + "x^" + str(len(values) - 1 - i) + " + "
        if values[-1] != 0:
            quotient += str(values[-1]) + " / (x - " + str(self.zero) + " )" 
        else:
            quotient = quotient[:-3]
        print(quotient)