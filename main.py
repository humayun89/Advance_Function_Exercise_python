# Initial division system :-
x=int(input(" Enter a number:-"))
y=int(input(" Enter a number :- "))
def div(x,y):
    return (x/y)
print(div(x,y))
""" div is not a variable , itself is a function . As a result we call the function in print rather than a varible in it."""

# Uses of lambda function:-
div =lambda x,y: x/y
print(div(3,2))

#  Using input :
x=int(input(" Enter a number:-"))
y=int(input(" Enter a number :- "))
div =lambda x,y: x/y
print(div(x,y))