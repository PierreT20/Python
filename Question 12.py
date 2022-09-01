def histogram():
    z = input('Enter a string: ')
    l = list(set(z))
    l.sort()
    count = 0
    print(z)
    for i in l:
        if i!= ' ' :
            count = z.count(i)
            print(str(i).upper(), end= ' ')
            print(count*'* ')
    

histogram()

