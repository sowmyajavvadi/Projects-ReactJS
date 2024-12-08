class student:
    school="python"
    def __init__(self,m1,m2,m3) -> None:
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    #get method is used to fetch the alue also know as accessors
    def get_m1(self):
        return self.m1
    #set method used to set the values
    def set_m2(self,value):
        self.m2 = value
        return self.m2


s1=student(11,23,23)
s2=student(45,67,78)

print(s1.avg())
print(s2.avg())
print('new m2 value:' , s1.set_m2(34))