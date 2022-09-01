#gallons = wall/115
#hours = gallons*8
#cost = paint*gallons
#labour = hours*20
#total = cost+labour
import math

def gallons(wall):
    gallons = math.ceil(wall/115)
    return gallons

def hours(gallons):
    hours = gallons(wall)*8
    return hours

def cost(paint,gallons):
    cost = paint*gallons(wall)
    return cost

def labour(hours):
    labour = hours(gallons)*20
    return labour

def total(cost,labour):
    total = cost(paint,gallons) + labour(hours)
    return total

wall = float(input("Enter wall space in suqare feet: "))
paint = float(input("Enter paint price per gallon: "))

print("Gallons of paint: ",gallons(wall))
print("hours of labor: ",hours(gallons))
print("Paint charges: $", cost(paint,gallons))
print("Labor charges: $", labour(hours))
print("Total cost: $",total(cost,labour))



