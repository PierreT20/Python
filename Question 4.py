
def milesToKilometers(Km):
    miles = Km*0.6214
    return miles

Km = float(input("Enter a distance in Km to be converted: "))

print("The conversion of",Km,"kilometers","to miles is", milesToKilometers(Km),"miles")
