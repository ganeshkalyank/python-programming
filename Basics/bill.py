units = 1
while units!=0:
  units = int(input("Enter no. of units: "))
  if units<100:
    charge = 100
  elif units in range(100,200):
    charge = 100+3*(units-100)
  elif units in range(200,500):
    charge = 100+300+5*(units-200)
  else:
    charge = 100+300+1500+10*(units-500)
  print("Charge:",charge)
