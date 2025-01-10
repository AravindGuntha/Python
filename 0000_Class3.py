# This is all about instance variables.
# Types of methods.
# Decorators.

# As discussed earlier, we have Class variables - Which are declared inside the class & outside the functions & are constant throughout all the objects 
# Note that these values can later be changes based on the need.

# Now, we'll talk about instance varaibles -> these are the kind of variables which are different from instance to instance (instance of the class) 
# To declare these, we need to create a __init__ function. => init function is a Constructor basically, which is used to initialization.
# we pass parameters to the init function. => these parameters are used as the variables & are called as instance variables.

# So, how do we call the init function ?? => do we need to explicitly say __init__() 
# The answer is NO, when we create a object, the init function is automatically called, all the parameters we pass while creating the object are passed as arguments to the 
# init function. 

# eg.;

class Bottle:
  brand = "Milton"  # Class Variable 1 
  logo  = "M"       # Class Variable 2

  def __init__(self, color, capacity): # as discussed self is the object address, which every method takes as the first argument to make sure which object is calling it.
    self.color = color                 # color & capacity are the parameters that are passed to the init function 
    self.capacity = capacity           # self.color & slef.capacity are object variables as self is the object here.
    print("Here is your {} coloured bottle with {} Liters of capacity".format(self.color,self.capacity))


b1 = Bottle("blue", 1) 
# b2 = Bottle()
# the above thing fails as the required parameters are not provided. 

# So, what if I've more parameters to send / what if i don't have no parameters to send.
# in the above cases, we need to create more __init__ functions based on your need, if __init__ with no parameters(just self) is created then, we create the object using 
# b2 = Bottle() 

# why do we call the constructor as an initiator or initialization method ?
# this is the method which is invoked or run when we create an object. 
# So, if there are a few things, which we wanted to create soon after creation of an object / while creating an object
# those things can go in here.
# Let's take the above example to understand. 
# we are creating a Bottle, irrespective of Capacity & Color, 
# we would definitely need to package it. So, we can make the packing infromation ready.
# Similarlly we wish to thank the customer for choosing our brand, we can do that 

# Let's suppose we are creating a To-do List: 
# then to hold all the Items we would need a List right, so, we can create that list in the init fucntion. & this can be later used in the other functions.

# eg.

class Diary:
  company = "Haathi"
  Pages = "500"

  def __init__(self, bind_color, model):
    self.bind_color = bind_color
    self.model = model
    self.todo_list = []

  def addToDo_Item(self, item):
    self.todo_list.append(item)

  def get_ToDoList(self):
    print(self.todo_list)

d1 = Diary("Green", "Ruled")
d1.addToDo_Item("Drink Water")
d1.addToDo_Item("Clean Room")
d1.get_ToDoList()
    

# so, what if we are not defining any __init__ functions, what happens then ? 
# there will be a default __init__ function created which doesn't take any arguments & just have the pass statment passed in the funntion. => this is called as Default Constructor.
# & the init functions where there are parameters mentioned, is called as parameterized constructor.

# note that, class varaibles can be reffered with class_name.variable_name / object_name.variable_name 
# instance variables can be reffered with Object_name.variable_name & all the other methods in side the class can use these variables.

# Now same applies to methods. 
# if a function uses only the class variables, we can convert that to a class method
# if a fucntion doesn't use any of the variables either the class or the instance types, then we can convert that to staticmethod. 

# note as we are saying specifically, class variables, it take Class as the first argument. (generally use cls)
# as we say staticmethod, it doesn't take any parameters / arguments. Not even the self argument (which is a object)

class Home:
    name = "Aravind's Villa"
    storage = 3

    def __init__(self, loc, facing):
        self.loc = loc
        self.facing = facing
        self.equipments_needed = ["lights","fans","wires","tiles","doors","handles"]

    @staticmethod
    def print_ready():
        print("The new flat is ready for use")
    
    
    @classmethod
    def marketing(cls, val1, val2):
        print('''We are beginning a new venture here & it's called as 
                 {} & storage capacity of this building is {} floors
              '''.format(cls.name, cls.storage))
                
home1 = Home("New Street", "East")
home1.print_ready()
home1.marketing()




  
