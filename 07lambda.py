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

#############################################################
#A REGULAR FUNCTION
def guru( funct, *args ):
  funct( *args )
def printer_one( arg ):
  return print (arg)
def printer_two( arg ):
  print(arg)
#CALL A REGULAR FUNCTION 
guru( printer_one, 'printer 1 REGULAR CALL' )
guru( printer_two, 'printer 2 REGULAR CALL \n' )
#CALL A REGULAR FUNCTION THRU A LAMBDA
guru(lambda: printer_one('printer 1 LAMBDA CALL'))
guru(lambda: printer_two('printer 2 LAMBDA CALL'))