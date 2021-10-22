myfile = open("FileProcessing\files\fruits.txt")
content = myfile.read()
myfile.close()

# file closed automaticly with "with" method
with open("FileProcessing/files/fruits.txt", "w") as myfile:
    
    content = myfile.read()
    
# writing text to file
with open("FileProcessing/files/vegetables.txt", "w") as myfile:
    myfile.write("Tomato\nCucumber\nOnion\n")
    myfile.write("Garlic")
    
    
def foo(character, filepath="FileProcessing/files/fruits.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)

with open("bear.txt", "w") as file:
    file.write("snail")

with open("FileProcessing/files/fruits.txt", "a+") as myfile:
    myfile.write("\nOkra")
    myfile.seek(0)
    content = myfile.read()
    
print(content)

