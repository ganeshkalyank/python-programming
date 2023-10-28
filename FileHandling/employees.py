import csv

emps =[["ID","Name","Salary"]]

op = "y"

while op == "y":
    emp = []
    for fld in emps[0]:
        emp.append(input("Enter "+fld+": "))
    emps.append(emp)
    op = input("Add another? (y/n):")

with open("employees.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(emps)
    print("Written successfully.\n")

with open("employees.csv","r") as file:
    reader = csv.reader(file)
    eid = input("Enter employee ID: ")
    found = False
    for row in reader:
        if row[0] == eid:
            print(row)
            found = True
    if not found:
        print("Employee not found!")
