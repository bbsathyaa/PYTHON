#errorTypes:Syntax error,Logical error(Exceptions)
#Syntax error
a,b=1,2
print(a ,b)                                  #SyntaxError: invalid syntax

#Exceptions
print(dir(locals()['__builtins__']))        #list of built-in exceptions

l1=list(range(5))
l1[7]                                       # IndexError: list index out of range
import module1                              #ModuleNotFoundError: No module named 'module1'
d1={'a':'1','b':'2'}
d1['c']                                     #KeyError: 'c'
from math import cube                       #ImportError: cannot import name 'cube' from 'math' (unknown location)
t1=iter([1,2])
print(next(t1))
print(next(t1))
print(next(t1))                             #StopIteration
print('hello'+2)                            #TypeError: can only concatenate str (not "int") to str
int('abc')                                  #ValueError: invalid literal for int() with base 10: 'abc'
print(d)                                    #NameError: name 'd' is not defined
print(12/0)                                 #ZeroDivisionError: division by zero

#exceptionHandling
try:
    l1 = list(range(5))
    l1[7]
except IndexError:
    print("list index out of range")
else:
    print("success")

try:
    import mod1
except ModuleNotFoundError:
    print("No module named 'module1'")

try:
    d1 = {'a': '1', 'b': '2'}
    d1['c']
except KeyError:
    print("Key not found")

try:
    print(d)
except NameError:
    print("name not found")

try:
    print(10/0)
except ZeroDivisionError:
    print("Division by zero")

#simpleCalculator
def calc():
    try:
        a=int(input("enter no1"))
        b=int(input("enter no2"))
        c=input("enter opertion:+,-,*,/")
        if(c=='+'):
            print(f"{a}+{b}={a + b}")
        elif (c == '-'):
            print(f"{a}-{b}={a - b}")
        elif (c == '*'):
            print(f"{a}*{b}={a * b}")
        elif (c == '/'):
            try:
                print(f"{a}/{b}={a / b}")
            except ZeroDivisionError:
                print("Division by zero")
        else:
            print("enter a valid input")
    except ValueError:
        print("enter a valid input")
calc()

#try block raises a nameError
try:
    print(d)
except NameError:
    print("name not found")
except:
    print("Error") 
 
#input inside try block
try:
    a=int(input("enter number"))
    print(a)
except ValueError:
    print("Enter interger value!")
