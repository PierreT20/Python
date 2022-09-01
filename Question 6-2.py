import random
def inCircle():
    r = random.randint(1,20)
    x = random.randint(-10,10)
    y = random.randint(-10,10)

    if (x*x + y*y) <= (r*r):
        print('True')
        print('Point',x,',',y,'is in circle with radius ',r)
    else:
        print('False')
        print('Point ','(',x,',',y,')','is not in circle with radius ',r)

inCircle()
