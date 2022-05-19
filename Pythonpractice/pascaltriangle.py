def pascal_triangle():
    num = 4
    for i in range(0,num):
        list = [1]
        term = 1
        k = 1
        for j in range(0,i):
            term = term*(i-k+1)/k
            list.append(term)
            k += 1
        print(list)

pascal_triangle()