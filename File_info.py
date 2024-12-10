# this is all about file operations.
# reading and writing the files.

# basic syntax is as below.
# file1 = open("File_Name(in case of same folder, else total path)", "mode") => default mode is read.
# mode should be a string, r => reading, 
#						   w=> writing,
#						   x=> create new file and open for writing,
#                          a => writing, appending at the end
#                          b => binary mode (rb => reading the binary file)
#                          t => text mode(by default)
#                          + => open a disk for updating (read & update the data)

# file1_data = file1.read() 
# file1_data = file1.read(n) => read the first n characters of the file.
# file1_line1 = file1.readline() => we can either do a complete read / read line by line. once the file is read completely, & when we try to read the line1 we get empty chars.
# file1.close() => to close the opened file. 


# to write the data. 
# we may completely delete the data and write the file / we may want to append the data 
# select the mode as per need, 
#            w => delete and write / a => to append to existing data.
# new_line = "This is the new Line i wanted to enter in the file"
# file1 = open("File1.txt", "w") / # file1 = open("File1.txt", "a")
# file.write(new_line) 
# file1.close()

# we also have modes such as
# r+ => read & write (without truncating, and pointer at the beginning, replaces character by character)
# w+ => Creates the file if not exist, read & write (truncates the data, and 


# other syntax to open the files.
#
# with open("File_Name", "mode") as File1:
#	data = File1.read()
# 	print(data)


# deleting the files.
# to delete the files, we would need some "modules" 
# module is nothing but a Pre-defined python code (library => basically collections of codes),
# written by some other programmer, which contains functions we can use to do our operations
# so, to add or install the non-existing package/module we can do
# pip/pip3 install package/module_name

# import package/module_name
# import os
# os.remove("File_Name")
