# Python I/O

# Opening and reading file the intuitive way
myFile = open("files/fruits.txt", "r")
print(myFile.read())
myFile.close()

# Managing resources using the 'with' statement
with open("files/fruits.txt") as myManagedFile:
    fileContent = myManagedFile.read()

print("\nManaged File Content:")
print(fileContent)

# Writing to file
with open("files/vegetables", "w") as writableFile:
    writableFile.write("Tomato\nCabbage\nCarrot")
    writableFile.write("\nGarlic")