def ReadFileLine(FileName, Search_String):
    with open(FileName, "r") as F1:
        data = " "
        Find = False
        while data:
            data = F1.readline()
            if(Search_String in data):
                print("String Found")
                Find = True
                break
        if(not(Find)):
            print("String Not Found")

def tot_words(File_Name):
    with open(File_Name, "r") as F:
        data = F.read()
    
    new_data = data.split("\n")
    new_data2 = []
    for items in new_data:
        new_data2 += items.split(' ')

    print(new_data2)
    return len(new_data2)
        
ReadFileLine("Sample.txt", "Learning")
print(tot_words("Sample.txt"))
