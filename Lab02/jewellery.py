gramrate = int(input("Gram rate: "))
weight = int(input("Ornament Weight: "))
exchange = int(input("Exchange weight: "))
wastage = int(input("Wastage (%): "))
gst = int(input("GST (%): "))

price = gramrate*((weight+((wastage+gst)*weight)/100)-exchange)

print("Price: ",price)
