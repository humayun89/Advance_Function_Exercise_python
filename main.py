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
""" Its not solve yet """
def multiply (input_list):
    result=1
    for i in input_list:
        result *= i
        for input_list in range(1,100):
            return result
print(multiply(my_list))