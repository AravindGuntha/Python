# is all about
# strings, length of string, indexing of string forward and reverse, slicing of string, few inbuilt string fucntions.

string1 = "Hello World !!"
print(type(string1))
print("The length of String1 variable is : ", len(String1))

# H    e    l    l    o         W    o    r    l     d     !     !
# 0    1    2    3    4    5    6    7    8    9    10    11    12
#-13   -12  -11  -10  -9  -8    -7   -6   -5   -4   -3    -2    -1

# this above is called as indexing, is used to read any specific character as per the need.
# also used to slice the string into different sub strings => we have to use the Indexes.
# string1[0] => reading the character at the 0th Index from the String1 variable. 
# String[x:y] => cutting the string starting from the xth index to (y-1)th index.
#             => if x or y is not provided the default value for the x is : 0 & y is len of the string.

String1 = "Hi !!"
mul = 3 
print(String1 * 3) # => this means, the Hi !!Hi !!Hi !!

String2 = "Hello."
print(String1 + String2) # => this will concatenate both the strings and provide the result as "Hi !!Hello."

string1.endsWith('er')   # => returns true of false
string1.capitalize()     # => makes the 1st character in the strings to Capitalize.
string1.replace("old", "new") # => replaces the old with the new
stirng1.find(word)       # => returns the index the word is starting at => returns -1 if the word is not found.
string1.count("am")      # => counts how many such sub-strings are there.


