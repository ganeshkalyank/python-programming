import os
filename = input("Enter file name: ")

try:
    if not os.path.exists(filename):
        raise FileNotFoundError(filename)
    file = open(filename, "w")
    file.write(input("Name: ")+", ")
    file.write(input("Rollno: ")+"\n")
    file.close()
except FileNotFoundError as fnfe:
    print("File not found:",fnfe)
