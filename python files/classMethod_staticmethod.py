class student:
    school="python"
    def __init__(self,m1,m2,m3) -> None:
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def get_school(cls):
        return cls.school
    @staticmethod
    def Info():
        print("print the static method for the students")

s1=student(11,23,23)
s2=student(45,67,78)

print(s1.avg())
print(s2.avg())
print('school name:' , student.get_school())
student.Info()