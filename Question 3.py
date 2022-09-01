def main():
    x = dict()
    y = dict()
    z = open("WorldSeries.txt","r")
    name = z.read().splitlines()
    x, y = series(name)
    series(name)
    Afunction(x,y)
    
def series(name):
    x = dict()
    y = dict()
    year = 1903
    for a in name:
        x[year] = a
        year = year + 1
    b = list(set(name.copy()))
    for a in b:
        y[a] = name.count(a)
    return x, y

def data(x,y):
    year = int(input("Enter a year in the range 1903-2020: "))
    if (year == 1904 or year == 1994):
        print ("The world series wasn't played in the year ", year)
    elif (year < 1903 or year > 2020):
        print ("The data for the year", year, "is not 1included 1n out database ")
    else:
        whoWon = x[year]
        number = y[whoWon]
        print("The team that won the world series in", year, "is the", whoWon)
        print ("They won the world series", number, "times ")

def Afunction(x,y):
    repeat = "y"
    while repeat == "y":
        data(x, y)
        repeat = input('Do you want to continue, type "y" for yes, or "n" for no: ')

main()
