# Create a function getting two integer inputs from user and print the following
#  Addition of two numbers is + value
# Subtraction of two numbers is + value
# Division of two numbers is + value
# Multiplication of two numbers is + value

def operations(a, b):
    sum1 = a + b
    sub1 = a - b
    mul1 = a * b
    div1 = a / b
    return sum1, sub1, mul1, div1


c = int(input("Enter the no "))
d = int(input("Enter the 2nd no "))
print(operations(c, d))


