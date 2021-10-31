# Python I/O
import time
import os
import pandas # pip install pandas - cmd prompt

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
with open("files/vegetables.txt", "w") as writableFile:
    writableFile.write("Tomato\nCabbage\nCarrot")
    writableFile.write("\nGarlic")

while True:
    # Check if the file already exists
    if (os.path.exists("files/vegetables.txt")):
        myFile = open("files/vegetables.txt", "r")
        print(myFile.read())
    else:
        print("File does not exist")
    time.sleep(4)
