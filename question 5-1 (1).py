def rectangle():
    x = int(input('Enter length of the first rectangle: '))
    z = int(input('Enter width of the first rectangle: '))
    c = int(input('Enter length of the second rectangle: '))
    v = int(input('Enter width of the second rectangle: '))

    areaA = x*z
    areaB = c*v
    print('Area of A = ',areaA)
    print('Area of B = ',areaB)

    if areaA > areaB:
        print('Area A is greater than area B')
    if areaB > areaA:
        print('Area B is greater than area A')
    else:
        print('Area A is equal to area B')

rectangle()

