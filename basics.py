# "#" anyline that has the # (not as a character in string) treated as a comment in python.
# python has dynamic type allocation
# meaning, the type of the variable is allocated in the process of run time

x = 5 # now the type of the x will be Int
x = "5" # now the type of the x will be String, so based up on the value of the variable python defines it's type of the variable
x = True # boolean
x = None # none type variable
x = 3.24 # floating integer.
x = -10 # int with negative value => possible.

x = 5 # python is case-sensitive meaning => a & A are treated differently
y = 6 
print("value of x is ",x) # print statment allows to display the content in the console.
print("value of Y is ",y)
print(x + y) # => arithmentic operation add 
print(x - y) # => arithmentic operation sub 
print(x * y) # => arithmentic operation multiply
print(x / y) # => arithmentic operation divide => automatically converts the result type to float
print(x ** y) # => arithmentic operation powerof

print(x > y) # Displays True / False Greater than operator 
print(x < y) # Displays True / False Less Than operator
print(x >= y) # Displays True / False Greater than or Equal to operator
print(x <= y) # Displays True / False Lessthan or Equal to operator
print(x == y) # Displays True / False is equal to operator
print(x != y) # Displays True / False Not equal to operator

x = 10
y = 20
z = "30"
# here the z type is string, as there are numbers in there, we can convert that manually to the int
z = int(z)

z += z # => z = z + z
x *= 2 # => x = x * 2
x **= 3 # => x = x ** 3 => x = x to the power of 3

print(x > y and x > z) # to concatinate two relational operations
print(x > y or x > z) # to concatinate two relational operations
print(not(x > y)) # a not operation provides the inverse of the result obtained.

#to ask the information from the user.

input("Please enter your name: ")
input("Please enter your age: ") 
# input always treats the information provided as a string, so, if we want to use it as different type we need to type cast it to the desired variable.
# So, to convert the age to a number we use the below snippet.
age = int(input("Please enter your age: "))
