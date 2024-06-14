# f(x) = x+10
x = lambda a : a + 10
print(x(5))

#############################################################

# f(a,b) = a*b
x = lambda a, b : a * b
print(x(5, 6))

#############################################################

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2) # it will duplicate any number
mytripler = myfunc(3) # it will triplicate any number

print(mydoubler(111))
print(mytripler(111))

#############################################################

# The second parenthesis means the argument of the lambda
print((lambda x: x + 1)(2))

# (lambda x: x + 1)(2) = lambda 2: 2 + 1
#                      = 2 + 1
#                      = 3

#############################################################

adder = lambda x, y: x + y
print(adder (500, 500))

#############################################################
#What a lambda returns #2
x="some kind of a useless lambda"
(lambda x : print(x))(x)