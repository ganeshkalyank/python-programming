class Parent:
    def __init__(self,x):
        self.pname = x

class Child(Parent):
    def __init__(self,x,y):
        super().__init__(x)
        self.cname = y
c = Child("I am Parent","I am Child")
print("Parent name:",c.pname)
print("Child name:",c.cname)
