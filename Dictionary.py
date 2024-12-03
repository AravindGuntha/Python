# we have an other type of variable in python called as dictionary
# dictionary is key value pair basically, => let's relate this to a real word Dictionary, like every dictioanary will have words and meaning attached to the word. 
# to know what the meaning is, we should know what the word is fare enough right, without konwing the Word what meaning are we looking for. So, we would first need the word only then we can know the meaning of it.
# To realte, Key is the word here and value is the meaning of it.
# 
# Ditcitonary can't contian the same key defined again.
# Ofcourse, one key can contain many values, but we can't have the same key defined multiple times.
# a value can be of any type : that is it can be a int, float, Boolean, string, List, tuple and dictionary itself.
# dictionary is immutable 
# we can also have a null dictionary aswell.
#

dictionary1 = {
  "Key1": "This is the value for Key1",
  "Key2": "This is the value for Key2",
  "Key3": "This is the value for the key3",
  1: "This is the integer Key - 1",
  2: "This is the integer key - 2",
  3: "This is the integer key - 3",
}

# as above we have the keys as strings and int, it's quite possible to have Float type of key aswell.

null_dict1 = {}
dict_profile ={
  "name": "Arya",
  "Age": 27,
  "Scores":{
    "Chem": 94,
    "Phy": 91,
    "Math": 100
  },
  "IdProofs": ("aadhar", "passport", "voter card"),
  "vehicles": ["fz", "punch mt",],
}

# to access the scores of specific subject we have to 2d array kind of representation.

print(dict_profile["Scores"]["Chem"])


dict1.keys() # => returns all the keys => this type returned is a special type => so, this can be type casted to a List / tuple
dict1.values() # => returns all the va lues. => this type returned is a special type => so, this can be type casted to a List / tuple
dict1.items() # => returns all the each keys & value pairs as tuples.
dict1.get("name") # this is equal to dict1["name"] => differnce is that, in the method way of accessing the value of a key, we'll not get error in case the key is not present.


