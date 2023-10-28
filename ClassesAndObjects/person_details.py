class Person:
    def showDetail(self):
        print("Aadhar ID:",self.__aadharId)
        print("Name:",self.__name)
        print("Address:",self.__address)
    @property
    def aadharId(self):
        return self.__aadharId
    @aadharId.setter
    def aadharId(self,aadharId):
        self.__aadharId = aadharId
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self,address):
        self.__address = address

p = Person()
p.aadharId = 123456789101
p.name = "Kalyan"
p.address = "Main Road, Velicheru"
p.showDetail()
