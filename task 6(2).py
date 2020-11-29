#2)Write a program to get the below pattern
#54321
#4321
#321
#21
#1

row=5
for i in range(0,row+1):
    for j in range(row-i,0,-1):
        print(j,end='')
    print()
