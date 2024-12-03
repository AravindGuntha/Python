# all about Lists and Tuples.
# sample codes too..

list1 = [1, 2, 3, 4, 5, 6, 7] # => list is a collection of variables. just like an array, 
list2 = [1, 2.2, 3.145, -4, "Hello", "End", True] #but can hold different type of variables too

# Similar to string, indexing is done & slicing is done.
# one main difference between lists and stirngs is that, Strings are immutable => meaning, value can't be changed via indexing.
#                                           where as the Lists are mutable => meaning, value can be changes via indexing.

stirng1 = "Hellow World !!" # string1[4] = "S" => Gives error as the string is immutable.
list1[4] = "How are you" # doesn't give any error as, it's mutable.

# list has few predefined or builtin fucntions, which we can use.
  # we can sort the list in ascending or descending order.

list1.sort(reverse=True) # => this says to sort the list1 in descending order.
list1.sort() #=> this says to sort the list1 in the ascending order.
list2.reverse() #=> this fucntion simply reverses the sequence of the list, meaning, the first item would be the last and last would be the first.
list2.append() #=> to add any element at the end of the existing list elements.
list2.insert(2, "New Element") #=> to add the element "New Element" at the 2nd index.
list.remove(val1) #=> removes the elements with the value = val1
list.pop(index1) #=> removes the element at index = index1



# Tuples.
# Tuple is a immutable thing, holds different values of different types. Once the tuple is created, it can't be changed.
tuple1 = (1, 2, 3, 4, 5, 56, 6) 
tuple1.index(56) # => to find the index of the element 56
tuple.count(5) # => finds how many times the element 5 is used.



# program to check if the list is a palindrome.
List1 = [1, 2, 3, 2, 1]
len = len(List1)
if(len % 2 == 0): 
  half_ind = int(len/2)
else:
  half_ind = int(len/2) + 1

if(List1[0] == List1[len] and List1[1] == List1[len-1]):
  print("it's palindrome")
else:
  print("not a palindrome")
