class Student:
    def __init__(self,name,rollno) -> None:
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()

    def show(self):
        print("name=",self.name +" rollno=",self.rollno)
        self.lap.show()
    class laptop:
        def __init__(self) -> None:
            self.ram='8'
            self.cpu='i5'
            self.brand='hp'
        def show(self):
            print("ram",self.ram +" cpu=",self.cpu)

s1=Student("sowmya", "412")
s2=Student("divya","413")
s1.show()
s2.show()
lap1=s1.lap.show()
lap2=s2.lap.show()
