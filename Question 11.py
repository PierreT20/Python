A = int(input("Enter a number: "))
B = int(input("Enter another number: "))
def NumbersInRange(A,B):
    acc = 0
    for x in range(A,B+1):
        print(x,end=" ")
        acc = acc + x
    print("\nsum of numbers: ",acc)

NumbersInRange(A,B)
