with open('01.in') as f:
    sum=0
    for x in f:
        r = (int(x)//3) -2
        while (r>0):
            sum+=r
            r = (int(r)//3) -2
    print(sum)
