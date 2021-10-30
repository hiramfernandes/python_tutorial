# Python I/O

# Opening file the intuitive way
myFile = open("files/fruits.txt")
print(myFile.read())
myFile.close()

# Managing resources using the 'with' statement
with open("files/fruits.txt") as myManagedFile:
    fileContent = myManagedFile.read()

print("\nManaged File Content:")
print(fileContent)