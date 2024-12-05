# This is all about sets.
# set is an other type of predefined data type, it is similar to that of the list, only difference is it doesn't hold duplicate values
# even though we try to enter the duplicate values, the set will only hold unique values.
# and main thing in the set is => set's order changes everytime, if you print the same set multiple times, the sequence of it changes.
# sets are mutable, but the elements in the sets are immutable. => meaning, we can't change the sets => so, set accepts int, float, string and tuple 
# Set can never hold the List and Dictionary, because, List and Dictonary are never immutable.

set1 = {1,2,3,4,5,5,6,6,6,7,7,88,8,9,9,9,90,88} # set is defined in this way
set2 = {1, 2, 3, "String", (1, 2, 3)}


null_set = set() # if we say null_set = {} => this is treated as an empty dictionary, so we can't use this.

set1.add("item_value")
set.remove("item_value")
set.clear() #  empties the total set.
set.pop() # removes a random value.

set1.union(set2) # union operation on both the sets
set1.intersection(set2) # performs intersection operation on both the sets
