x = float(input("Enter the total sales for the month: "))
StateTax = x*(1/100*4)
CountyTax = x*(1/100*2)
TotalTax = StateTax + CountyTax

print("Monthly sales: $",x)
print("State tax: $",StateTax)
print("County tax: $",CountyTax)
print("Total tax: $",TotalTax)
