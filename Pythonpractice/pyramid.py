def num_pyramid(n):   
    for i in range(n):
        for j in range(i + 1):
           print("*",end = " ")
        print()
    
num_pyramid(5)