Input = ['Facebook', 'Google', 'Google']

for i in Input:
    if Input.count(i)>1:
        print(i)
        break

Input = ['Facebook', 'Facebook', 'Google', 'Google']

for i in Input:
    if Input.count(i)>1:
        print(i)
        break

Input = [ 'Google', 'Facebook', 'Facebook', 'Google']
Input.sort()
for i in Input:
    if Input.count(i)>1:
        print(i)
        break
