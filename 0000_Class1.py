# this is an comprehensive introduction to the OOPS (Object Oriented Programming Language). 
# the traditional approach we follow is procedural programing => where in all the instructions are executed in the sequence.
# then we later developed the functional programing, where in we define the function, and can later use / execute those functions based on the need.
# by using the functional programming we obtain -> redundancy (meaning: we reduce the coding by just add all the code into the function.)
# by using the functional programming we obtain -> reusability (meaning: we use same set of code lines again and again by just calling the funciton.)
# to add an other layer of Re-usability & Redundancy we move to the OOPs.

# in this OOPS programing, we treat everything as objects; where in the Objects are actually the instances of the class. 
# meaning -> we first define the class; which is actually like a blue print or design of anything we need to create.
# we then, later use this desing & start creating the instances, & those instaces are called as the Objects.

# A class can contain any number of functions. So, as the object contains. 
# Thus by creating an object we are re-using all the functions created once in Class.

# the following is the classes definition & objects creation.

#defining the class
class Doors: #Doors here is the name of the class, and we should certainly name the class with Upper Case letters.
  length = 6                  
  breadth = 7
  width = 0.25
  color = "white"         
  
# every item we wanted to desing will definitely have some properties & behaviour, meaning the class(desing) will definitely have some properties and some behaviour
# to elaborate; let's suppose we are creating / designing a Bukcet => so, in reality every bucket would have
#   a color, size, capacity., etc => these are called as the properties of that bucket
#   similarlly, it might have functionalities, that would cool the water, or hot the water, that can freeze the water, may by with a click it can change the colors too => all these comes under the behaviours of the class
#   so, every item we wanted to desing, should have the properties & behaviours.. 


# so, in the above Doors class, length, breadth, width & color are called as the Properties.
door1 = Doors()     # "door1" is the Object Name & it's Object/Instance of the class Doors

# this is how we access the properties of the class / object.
print(door1.length)

