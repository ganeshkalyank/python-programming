class Textile:
    def getDet(self):
        self.type = input("Enter type: ")
        self.size = input("Enter size: ")
        self.colour = input("Enter colour: ")
        self.qty_on_hand = int(input("Enter quantity: "))
        self.rate = int(input("Enter rate: "))

    def putDet(self):
        print(self.type)
        print(self.size)
        print(self.colour)
        print(self.qty_on_hand)
        print(self.rate)

def getNetval(textiles):
    val = 0
    for t in textiles:
        val += (t.qty_on_hand)*(t.rate)
    print(val)

def main():
    textiles = []
    for i in range(2):
        t = Textile()
        t.getDet()
        textiles.append(t)
    getNetval(textiles)

if __name__ == "__main__":
    main()
