def longest_string(strings):
    strings.sort(key=len)
    return strings[-1]

n = int(input("Enter no. of strings: "))
strings = []
for i in range(0,n):
    string = input("Enter string "+str(i+1)+": ")
    strings.append(string)
print("Longest string:",longest_string(strings))
