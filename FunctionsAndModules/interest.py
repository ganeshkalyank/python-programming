def interest_cal(principal, interest_rate, years):
    simple_interest = years*principal*(interest_rate/100)
    x = 100/interest_rate
    print("Principle will double in",x,"years")
    return simple_interest

princ = int(input("Enter principal amount: "))
ir = int(input("Enter interest rate: "))
yrs = int(input("Enter years: "))

print("Simple Interest:",interest_cal(princ,ir,yrs))
