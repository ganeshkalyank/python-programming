class GroceryStore:
    def __init__(self):
        self.ItemId = input("Enter Item ID: ")
        self.ItemName = input("Enter Item Name: ")
        self.Rate = int(input("Enter Rate: "))
        self.StockInHand = int(input("Enter stock in Hand: "))
        self.ReorderLevel = int(input("Enter reorder level: "))

class StationaryItems(GroceryStore):
    def __init__(self):
        super().__init__()
        self.brand = input("Enter brand: ")
    def addNewItem(self):
        n = int(input("Enter quantity: "))
        self.StockInHand += n
    def sellItems(self):
        n = int(input("Enter quantity: "))
        if n > self.StockInHand:
            raise Exception("Insufficient stock")
        if self.StockInHand == 0:
            raise Exception("Item not available")
        self.StockInHand -= n
        if self.StockInHand < self.ReorderLevel:
            self.StockInHand += 0.5*self.StockInHand
            raise Exception("Item stock below Reorder level")

class SoftDrinks(GroceryStore):
    def __init__(self):
        super().__init__()
        self.manufacturer = input("Enter manufacturer: ")
    def addNewItem(self):
        n = int(input("Enter quantity: "))
        self.StockInHand += n
    def sellItems(self):
        n = int(input("Enter quantity: "))
        if n > self.StockInHand:
            raise Exception("Insufficient stock")
        if self.StockInHand == 0:
            raise Exception("Item not available")
        self.StockInHand -= n
        if self.StockInHand < self.ReorderLevel:
            self.StockInHand += 0.5*self.StockInHand
            raise Exception("Item stock below Reorder level")

def main():
    si = StationaryItems()
    sd = SoftDrinks()
    op = -1
    while op!=0:
        print("1. Add Stationary")
        print("2. Add Soft Drinks")
        print("3. Sell Stationary")
        print("4. Sell Soft Drinks")
        print("0. Exit")
        op = int(input("Choose an option: "))
        match op:
            case 1:
                try:
                    si.addNewItem()
                except Exception as e:
                    print(e)
            case 2:
                try:
                    sd.addNewItem()
                except Exception as e:
                    print(e)
            case 3:
                try:
                    si.sellItems()
                except Exception as e:
                    print(e)
            case 4:
                try:
                    sd.sellItems()
                except Exception as e:
                    print(e)
            case _:
                print("Invalid option!")
                

if __name__ == "__main__":
    main()
        
