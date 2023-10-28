count = 0
for i in range(int(input("Enter no. of students: "))):
    student = input("Enter student "+str(i+1)+" name: ")
    if len(student.split(" ")) == 2:
        count += 1
        
print("Student count with two worded name:",count)
