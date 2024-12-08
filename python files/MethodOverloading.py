class Student:
    def __init__(self,m1,m2) -> None:
        self.m1=m1
        self.m2=m2
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s

        
s1=Student(12,2)
s2=Student(47,6)
# we cannot give same names to the methods in pythin so method overloading is not possible but we use the "None type" to achive the method overloading
print(s1.sum())
print(s1.sum(12,2))
print(s1.sum(1,2,3))

