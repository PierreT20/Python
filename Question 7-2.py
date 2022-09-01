x = input('Enter a string: ')
r = int(input('Enter the number of repitions: '))

def repl():
    z = ''

    if r <=0:
        return x
    for i in range(r):
        z = z + x
    return z

print(x,'--->',repl())
