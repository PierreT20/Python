ClassA = 15
ClassB = 12
ClassC = 9

def incomeOfA(x):
    incomeA = ClassA*x
    return incomeA

def incomeOfB(z):
    incomeB = ClassB*z
    return incomeB

def incomeOfC(v):
    incomeC = ClassC*v
    return incomeC

def TotalIncome(incomeOfA,incomeOfB,incomeOfC):
    Total = incomeOfA(x) + incomeOfB(z) + incomeOfC(v)
    return Total

x = float(input("Enter count of A seats: "))
z = float(input("Enter count of B seats: "))
v = float(input("Enter count of C seats: "))

print("Income from Class A seats: ",incomeOfA(x))
print("Income from Class B seats: ",incomeOfB(z))
print("Income from Class C seats: ",incomeOfC(v))
print("Total income: ",TotalIncome(incomeOfA,incomeOfB,incomeOfC))
