#3)Python Program to Print the Fibonacci sequence

def fib(n):
    if(n==0):
        return 0
    elif(n==1):
         return 1
    else:
        return(fib(n-2)+fib(n-1))
n=int(input("enter the value of n \t"))
print("Fibonacci series \t",end='')
for n in range(0,n):
    print(fib(n),end='')
