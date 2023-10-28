mydict = {}

op = 0

while op!=4:
    print("1. Add student / Update student")
    print("2. Search student by name")
    print("3. Search student by regno")
    print("4. Exit")
    op = int(input("Enter an option: "))
    match op:
        case 1:
            regno = input("Enter register no: ")
            name = input("Enter name: ")
            mydict[regno] = name
            print("Student added / updated successfully!")
        case 2:
            name = input("Enter name: ")
            for key,value in mydict.items():
                if value.find(name) != -1:
                    print("Name:",value)
                    print("Register no:",key)
        case 3:
            regno = input("Enter register no: ")
            if mydict[regno]:
                print("Name:",mydict[regno])
                print("Register no:",regno)
        case 4:
            print("Exiting...")
