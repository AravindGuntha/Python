def Fun_Replace(File_name, Old_string, New_string): # function to replace old_string with new_string
  # here File_name, Old_String, New_String are all the parameters for this funciton.
    with open(File_name, "r") as F1: # with is an other way of opening the file, benefit is that we need not explicitly close the file.
        data = F1.read() # not much a difference while reading or writing operations
    
    new_data = data.replace(Old_string, New_string)

    with open(File_name, "w") as F1: # as "with" file operation implicitly closes the file, we can direclty open the file again.
        F1.write(new_data)

def File_Find(File_name, Search_string):
    with open(File_name, "r") as F1:
        data = F1.read()
        if(data.find(Search_string) != -1): 
            return "Data Found !!"
        else: 
            return "Data Not Found !!"


Fun_Replace("Sample.txt", "Baasha", "Language") # => Calling the funciton.
Fun_Replace("Sample.txt", "Python", "Java")
print(File_Find("Sample.txt", "Java"))
