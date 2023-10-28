mydict = {
    1: 20,
    2: 35,
    3: 50
}

emps = [["Kalyan",1,"SE",10000],["Ganesh",2,"SA",20000]]

emptypes = ("SE","SA","DBA","PM","QA")

for emp in emps:
    if emp[2] not in emptypes:
        print("Employee type invalid")
    else:
        print("Name:",emp[0])
        print("No. of Projects:",emp[1])
        print("Role:",emp[2])
        print("Incentive:",emp[3]*mydict[emp[1]]/100)

