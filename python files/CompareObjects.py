class Information:
    def __init__(self) -> None:
        self.age=20
        self.name="sowmya"
    def compare(self, c2):
        if(self.age == c2.age):
            print("both are same")
        else:
            print("different objects")
    

c1=Information()
c2=Information()
c2.age=90


c1.compare(c2)
print(c1.age)