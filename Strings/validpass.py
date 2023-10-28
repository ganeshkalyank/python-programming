def validate_password(password):
    uppercase = []
    for i in range(ord("A"), ord("Z")+1):
        uppercase.append(chr(i))
        
    lowercase = []
    for i in range(ord("a"), ord("z")+1):
        lowercase.append(chr(i))
        
    digits = []
    for i in range(ord("0"), ord("9")+1):
        digits.append(chr(i))
        
    spchars = ["*","#","$"]
    
    twodigits = []
    for i in range(0,100):
        twodigits.append(f"{i:02}")
    
    if len(password) < 8 or len (password) > 20:
        return "Length should be between 8 and 20"
    
    for p in password:
        if p not in uppercase+lowercase+digits+spchars:
            return "Invalid characters found"
    
    count = 0
    for u in uppercase:
        count += password.count(u)
    if count < 1:
        return "No uppercase letter found"

    count = 0
    for l in lowercase:
        count += password.count(l)
    if count < 1:
        return "No lowercase letter found"

    count = 0
    for sc in spchars:
        count += password.count(sc)
    if count == 0:
        return "No special character found"
    
    if count > 1:
        return "Only one special character is allowed"

    count = 0
    for d in digits:
        count += password.count(d)
    if count < 2:
        return "Minimum two digits are required"

    count = 0
    for td in twodigits:
        count += password.count(td)
    if count > 0:
        return "Consecutive digits found"

    return "Password is valid"

while True:
    password = input("Enter password: ")
    print(validate_password(password))
