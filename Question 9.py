def getData():
    l=[]
    l1=[]
    print("Enter highest temperatures for each month of the year.")
    for i in range(12):
        l1.append(int(input(f"Month {i+1}:")))
    l.append(l1)
    l1=[]
    print("Enter lowest temperatures for each month of the year.")
    for i in range(12):
        l1.append(int(input(f"Month {i+1}:")))
    l.append(l1)
    return l

def averageHigh(lst):
    s=sum(lst[0])
    a=s/12
    return a

def averageLow(lst):
    s=sum(lst[1])
    a=s/12
    return a  

def highTemp(lst):
    num=lst[0][0]
    for i in lst[0]:
        if(i>num):
            num=i
    return num

def lowTemp(lst):
    num=0
    for i in range(12):
        if(lst[1][i]<lst[1][num]):
            num=i
    return num

data=getData()

print("List of the highest and lowest temperatures for each moth of the year")
for i in data:
    for j in i:
        print(j,end=' ')
    print()
print("Average high temperature for the year",averageHigh(data))
print("Average low temperature for the year",averageLow(data))
print("Highest high temperature for the year",highTemp(data))
print("lowest low temperature for the year",data[1][lowTemp(data)])
