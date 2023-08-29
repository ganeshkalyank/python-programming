import stringModule as sm

print("a. Make Lower")
print("b. Make Upper")
print("c. Find Length")
print("d. Replace content")
op = input("Choose option: ")

string = input("Enter string: ")
match op:
    case "a":
        print("Lower:",sm.toLower(string))
    case "b":
        print("Upper:", sm.toUpper(string))
    case "c":
        print("Length:", sm.findLength(string))
    case "d":
        print("Replaced:", sm.replaceText(string))
