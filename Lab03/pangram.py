def isPangram(string):
    alphabets = []
    for i in range(ord("a"),ord("z")+1):
        alphabets.append(chr(i))
    for alphabet in alphabets:
        if string.find(alphabet) == -1:
            return False
    return True

x = input("Enter a string: ")
print("Is Pangram:",isPangram(x))
