name = input("Name: ")
try:
    rollno = int(input("Rollno: "))
    if rollno <= 0:
        raise Exception("Invalid Roll No")
except Exception as e:
    print(e)
