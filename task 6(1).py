#1)Write a program to loop through a list of numbers and add +2 to every value to elements in list

l1=[1,2,3,4,5]
print("original list ",l1)
l2=[]
for i in range(0,len(l1)):
    l2.append(l1[i]+2)
print("resultant list is ",l2)

