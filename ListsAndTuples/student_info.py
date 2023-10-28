students = []
studentscopy = []

option = "0"

while option!="6":
    print("1. Append student")
    print("2. Remove student")
    print("3. View student")
    print("4. Copy list")
    print("5. Remove all")
    print("6. Exit")
    option = input("Choose an option: ")

    match option:
        case "1":
            student = []
            x = input("Enter student name: ")
            student.append(x)
            x = input("Enter student roll no: ")
            student.append(x)
            x = input("Enter elective chosen: ")
            student.append(x)
            students.append(student)
            print("Student added")
        case "2":
            x = input("Enter student roll no: ")
            for student in students:
                if student[1] == x:
                    students.remove(student)
            print("Student removed")
        case "3":
            x = input("Enter student name: ")
            for student in students:
                if student[0] == x:
                    print(student[0],student[1],student[2])
        case "4":
            studentscopy = students
            print("List copied to studentscopy")
        case "5":
            students = []
            print("All students removed")
