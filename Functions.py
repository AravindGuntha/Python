# functions are just a block of code.
# if it's just a block of code, why is needed to be written as a function.
# well, the catch is that, the block of code which is written in the function can be called anywhere in the whole code.
# and can be executed any number of time we need with just a simple line.

# the following the syntax for the function.
# def funtcion_name(parameters...):     => this here is called the defenition of the function. it's not executed unitl and unless it's called. 
# (calling a function is just asking the system to execute the block of code inside the function)
#      block of code.  => to execute this block of code, we just say. function_name(parameters...)

def addition(x,y):  # x and y are called as the arguments/ paramenters. we can also have the paramenters set to a default value.
  return x+y         # these two lines combinely called as definition of the function. return is sending out a result.
 
z = addition(5,3) # this is calling the funciton.
print(z)

def add(x,y=5): # here x is normal parameter & y is the default parameter. => meaning, while calling the fucntion if the second paramenter is not mentioned, then it's default will be 5
  return x+y 

add(6,9) # gives the result as 15
add(6) # will give the result as 11 (as second paramter is considered as 5)

# finding the factorial of any given number, using the function.
def factorial(n):
  result = 1 
  for i in range(n,1, -1):
    result *= n
  return result








  


