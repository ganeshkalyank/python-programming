try:
    n = int(input("Enter a number (0 to 10): "))
    if n<0 or n>10:
        raise OverflowError("Number not in range.")
except OverflowError as oe:
    print(oe)
