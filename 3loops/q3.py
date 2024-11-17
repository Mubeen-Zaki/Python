def table(n):
    for i in range(1,11):
        if i == 5:
            continue
        else:
            print("{} * {} = {}".format(n,i,n * i))

table(5)