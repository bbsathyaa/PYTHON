#merged list of tuples from two lists
l1=list(range(5))
l2=list(range(5,10))
t1=list(zip(l1,l2))
print(t1)

#merge list and range to create list of tuples
l=range(1,8)
l1=["a","b","c","d","e"]
print(list(zip(l,l1)))

#sorting the list
l=list(range(10,0,-1))
print(sorted(l))

#filter odd numbers
l1=range(1,21)
l=list(filter(lambda n:n%2!=0,l1))
print(l)
