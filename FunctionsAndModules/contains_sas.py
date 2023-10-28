def contains_sastra(string):
    if string.find("sastra") != -1:
        return True
    return False

x = input("Enter a string: ")
print("Contains sastra:",contains_sastra(x))
