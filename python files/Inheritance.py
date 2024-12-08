class parent:
    def feature1(self):
        print("parent feature1")
    def feature2(self):
        print("parent feature2")
class Child(parent):
    def feature3(self):
        print("child feature3")
    def feature4(self):
        print("child feature4")
class subChild(Child):
    def feature5(self):
        print("child feature5")
    
a1=parent()
a2=parent()

a1.feature1()
a1.feature2()

a2.feature2()

b1=Child()

b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

c1=subChild()
subChild.feature5(c1)

