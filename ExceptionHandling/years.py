try:
    i = int(input("Enter starting year: "))
    j = int(input("Enter ending year: "))
    if i>=j:
        raise OverflowError("Starting year greater than or equal to ending year.")
    print(list(range(i,j)))
except OverflowError as oe:
    print(oe)
