def DataReader():
    file1=open('data.txt','r')
    Lines=file1.readlines()
    count=0
    l6=[]
    l=[]
    l2=[]
    l3=[]
    l4=[]
    l5=[]
    for line in Lines:
        l.append(line.strip())
    for p in l:
        l2=[]
        l2=p.split()
        for i in range(len(l2)):
            l2[i]=float(l2[i])
        l3.append(l2)
    for i in l3:
        l4=[]
        for j in l3:
            k=pow((pow((j[0]-i[0]),2)+pow((j[1]-i[1]),2)),1/2)
            l4.append("{:.2f}".format(k))
        l5.append(l4)

    print("      p1     p2    p3     p4     p5     p6     p7     p8")
    for i in range(len(l5)):
       print("P"+str(i)+"   "+'   '.join(map(str, l5[i])))

DataReader()

