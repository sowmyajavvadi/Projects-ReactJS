class parent:
    #class parent constructor
    def __init__(self) -> None:
        print("print init in paent class")
    def feature1(self):
        print("parent feature1")
    def feature2(self):
        print("parent feature2")
class Child(parent):
    def __init__(self) -> None:
        super().__init__()
        print("print init in child class")
    def feature3(self):
        print("child feature3")
    def feature4(self):
        print("child feature4")

a1=Child()
# Child.feature1(a1)
# Child.feature2(a1)
# Child.feature3(a1)
# Child.feature4(a1)