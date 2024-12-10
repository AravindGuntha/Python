NewFile = open("Sample.txt", "w") # opening the file in writing mode, if not exist will create, if exists, truncates to 0 chars and opens for writing
Line1 = "Hi Everyone\n"
Line2 = "we are Learning File ops\n"
Line3 = "Using the Java Language\n" # if the \n escape character is not mentioned, each character will be apended to the last character.
Line4 = "I Love using the Java Language" 
NewFile.write(Line1) 
NewFile.write(Line2)
NewFile.write(Line3)
NewFile.write(Line4)
NewFile.close() # to close the file. Explicitly
