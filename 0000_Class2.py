# This is an extension to the Classes.
# So, Once we design, we can create N-Number of Objects with that Desing.
# Now, when we create N-Number of objects, each and every object may not have the same properties / behaviours
# like when we create a Car Desing, some cars might have the external stephanie, some might not have. Some might have max speed of 180, some other might have different max speeds.
# but, few things are costant through out. 
# like the brand, tyres used, speakers company etc.

# we would definitely need to differentiate the Constant things & Object specific things.
# thus, with respect to the variables (Properties) we can classify those to Class Variable (which are constant for all the objects) & Instance Varables (Object Variables are specific to object)
# to define the class variables, define all the variables in the class (not inside any method).


class Jewellery:
  material = "gold"
  brand = "XYZ"

# In the above class; material is "gold" 
#                   & brand is "XYZ" for all the Jwellery Objects. 
# So, these two variables are called as Class Variables. & remain constant through out all objects
# 

jewel1 = Jewellery()        # creation of the object.
print(jewel1.material)      # object_name.class_variable is how we retrieve the class variables.
jewel1.material = "Silver"  # we can also re-initiate those variables.
print(jewel1.material)        


# so, for methods too, we have Instance Method,
#                              Class Method, 
#                              Static method. 
# Let's learn these differences starting with the basics of methods.

# as said earlier, methods are also called as behaviours, 
# & these are functions defined inside the class.

class Car:
    brand = "Renault"
    tyre_brand = "MRF"
    speaker_brand = "JBL"

    def carPlay(ObjectName):  
        # class is just a blueprint. All the Properties & Behaviours can be executed by a object only.
        # so, while we want to execute a method => we need to say for which object we are intending to run that method.

        # thus, we provided a parameter ObjectName for that function.
        # everyfunction needs one parameter, that accepts the ObjectName (can be anything.)
        print("this object has the Carplay")

car1 = Car() # this is object creation. 
Car.carPlay(car1) # this is calling the carPlay Method for car1 object. 

# to call any method, we would need to pass the ObjectName for the system to know 
# on which object we are running the method

# we can also call the method in the below way. 

car1.carPlay() # both the ways are right, while we say Object_Name.method()

# if we use the above way of calling the method, it sends the car1 as a parameter to that funciton, 
# & therefore, we need not explicitly code the objectName.
