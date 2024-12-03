# if, else 
# if elif & else
# nested if and else
# examples.

# these are called as conditional statments, which is used to decide the flow of the code.
# lets suppose we wanted to start the play, if it's not raining, so, in this case, we'll study the weather and decide what to do. please see the below to do this.

weather = "Not Raining"
weather2 = "About to Raining"
if(weather == "Raining"): # => it's written like if(some condition) => if the condition is true the code inside the block is executed.
  print("It's raining and we can't play now")
else:                     # if the condition is not true this code block is executed.
  print("It's not raining and we can start our play now")

# if we wanted to check multiple conditions we can do this
if(weather == "Not Raining"):
  print("It's not raining")
elif(weather2 == "About to Raining"): # if the first condition is false, checks this, if the first condition is true this is never checked.
  print("It's about to rain, please plan a shorter match")
elif(weather2 == "Two hours to rain"): # if all the abovee conditions are false only then checks this
  print("We've two hours for rain to come in, can play a medium range match")
else: # if all the abovee conditions are false only then checks this
  print("No sign of rain, you can plan a bigger match")


