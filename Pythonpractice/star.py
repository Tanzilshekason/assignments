i = 0
j = 16
for row in range(0,5):
    for col in range(0,17):
        if(row==col or (row==3 and (col==5 or col==11)) or (row==2 and(col==6 or col==10
        )) or (row==1 and (col==7 or col==9)) or(row==0 and col==8)):
            print("*",end="")
        elif(row==i and col==j):
            print("*",end="")
            i = i+1
            j = j-1
        else:
            print(" ",end="")
    print()
 





