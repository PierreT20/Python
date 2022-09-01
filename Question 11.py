T = {'CS101':3004,'CS102':4501,'CS103':6733,'NT110':1244,'CM241':1411}
E = {'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
J = {'CS101':'5:00am','CS102':'9:00am','CS103':'10:00am','NT110':'11:00am','CM241':'1:00pm'}

U = input('Enter a course number: ')
if U in T:
    print('The details for the course ', U, 'are: ')
    print('Room: ', T.get(U))
    print('Instructor: ', E.get(U))
    print('Time: ', J.get(U))
else:
    print(U, 'is an invalid course number')
