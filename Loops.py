# this code is all about the loops,
# this has While Loop


# syntax : while(condition is true):
#              {execute a block of statements that follow the indentation}
# below is the example.

i = 10
while(i >= 0):
  print("Hello world", i)
  i -= 1

# any time you want to develop the inner block of the code in the later, we can just initiate the main block and use the "pass" statement to leave the main without any operation.
# see below the example.

for el in range(1,10,2):
  pass # this is more like a dummy block, this doesn't execute.

# while with break
list1 = [1, 2, 3, 4, 5, ,6 ,7, 8, 9, 10]
j = 1
key = 7
while(j < len(list1)):
  if(list1[i] == key):
    break  # when a break statement is found, the system stops the execution then and there and comes out of that loop execution.
  else:
    i += 1
    continue # when a continue statement is found; the system immediately stops that current iteration and goes to the next iteration.

# for loop 
# for loop to traverse the lists, tuples or strings.

for el in list1:
  print(el)  # these two lines in total would print all the elements in the list1.

# for else loop. Which is basically used to find an element and perform and operation on that element or if it's not found what should be done.

list1 = [1,2,3,4,10,24,5,6,677,65,]
key = int(input("please enter the variable to search in the list : "))

for el in list1:
  if(el == key):
    print("The element 10 is found")
    break
  else: # while using the else for the if Clause; we should essentially indent that, parallel to where the if clause is starting.
    print("this else statement is related to the if")
else: #while using the else => if you want to allocate the else statement for the "FOR" loop we would need to indentate that parallel to where the for loop is starting"
  print("this else statement is related to the for")
  print("the list traversal is done & element is not found in the List")

# we have something called as a range; which is a range of values; where the value are mentioned in range.
# syntax is : range(starting_number, ending_number, increment/ step)
# for eg : if it's written range(6,16,2) => the values it shows are : 6,8,10,12,14 (16 will not be included)
# if we just say range(x,y) starting from x thru y with increment of 1
# if we just say range(x) starting from 0 thru y with increment of 1

list2 = range(10) 
print(type(list2)) # => here the type of that variable is "range"
print(list2) # => this will show => range(0,10)
for el in list2:
  print(el) # => this will print, every element starting from 0 thru 9, the last limit is excluded.


# program to find the factorial of a number.

n = int(input("please enter the number to calculate the factorial"))
factorial=1
for i in range(n,1,-1):
  factorial = factorial * i
else:
  print("the factorial for the number",n,"is : ",factorial)




