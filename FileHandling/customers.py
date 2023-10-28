def writeData():
    with open("customer.txt","a") as file:
        for i in range(5):
            print(f"Customer {i+1} details: ")
            file.write(input("Enter name: ")+", ")
            file.write(input("Enter address: ")+", ")
            file.write(input("Enter email id: ")+", ")
            file.write(input("Enter age: ")+"\n")
        
def readData():
    with open("customer.txt") as file:
        print("Name\tAddress\tEmail\tAge")
        for line in file:
            line = line.replace("\n","")
            line = line.split(",")
            print(line[0]+"\t"+line[1]+"\t"+line[2]+"\t"+line[3])

def main():
    writeData()
    readData()

if __name__ == "__main__":
    main()
