import registration as r

op = "0"

while op != "4":
    print()
    print("1. Register")
    print("2. Get By RegNo")
    print("3. Get By Programme")
    print("4. Exit")
    op = input("Enter any option: ")
    print()
    match op:
        case "1":
            r.register()
        case "2":
            r.getByRegisterNo(input("Enter RegNo: "))
        case "3":
            r.getByProgramme(input("Enter Programme: "))
        case "4":
            print("Exiting...")
