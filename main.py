# Initial division system :-
x = int(input(" Enter a number:-"))
y = int(input(" Enter a number :- "))


def div(x, y):
    return (x / y)


print(div(x, y))
""" div is not a variable , itself is a function . As a result we call the function in print rather than a varible in it."""

# Uses of lambda function:-
div = lambda x, y: x / y
print(div(3, 2))

#  Using input :
x = int(input(" Enter a number:-"))
y = int(input(" Enter a number :- "))
div = lambda x, y: x / y
print(div(x, y))


# Again:

def mul(x, y):
    return x * y


print(mul(3, 2))
"""Using lambda function."""
mul_lambda = lambda x, y: x * y
print(mul_lambda(3, 4))


# Multiplying my list :
def multiply(input_list):
    result = 1
    for element in input_list:
        result *= element
    return result
my_list = [1, 2, 3]
print(multiply(my_list))
# Go for more :'
""" Its not solve yet 
def multiply (input_list):
    result=1
    for i in input_list:
        result *= i
        for input_list in range(1,100):
    return result
print(multiply(my_list)) """

# Functions args and kwargs Exercise Solution:
def multiply_all(*args):
    m = 1
    for i in args:
        m *= i
    return m


test_1 = (1, 4, 3, 10)
multiply_all(test_1)

test_2 = (3, 5, 15, 2)
multiply_all(test_2)

test_3 = (2, 3, 8, 4)
multiply_all(test_3)
print(multiply(test_1))
print(multiply(test_2))
print(multiply(test_3))