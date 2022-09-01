m = 0
Sum = 0
x = int(input("Enter number of years: "))

while x < 1 or x > 10:
    x = int(input("Enter number of years: "))
    if x < 1 or Y > 10:
        print("Invalid years..!!!")

for i in range(Y):
    print("For year", i+1," : ")
    for j in range(12):
        print("Enter Rainfall in month", i+1, ": ", end =' ')
        z = float(input())
        Sum = Sum + z
        m = m + 1

Avg = Sum/m

print("Total rainfall = ", float(Sum), "inches")
print("Average rainfall per month = ", float(Avg), "inches")
