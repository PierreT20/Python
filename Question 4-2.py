import random
def numberCount():
    even = 0
    odd = 0
    for numbers in range(0,100):
        r = random.randint(1,1000)
        if (r % 2) !=0:
            odd = odd + 1
        else:
            even = even + 1
    print('Out of 100 numbers,',odd,'were odd, and',even,'were even')

numberCount()

