attendees = []

def register():
    attendee = []
    for field in ["reg no", "name", "programme", "willingness (y/n)"]:
        attendee.append(input("Enter "+field+": "))
    global attendees
    attendees.append(attendee)

def getByRegisterNo(regno):
    for attendee in attendees:
        if attendee[0] == regno:
            print(attendee)
            return
    print("Not found")

def getByProgramme(programme):
    for attendee in attendees:
        if attendee[2] == programme:
            print(attendee)
