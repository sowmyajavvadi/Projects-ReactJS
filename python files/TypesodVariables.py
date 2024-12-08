class car:
    #class/static variables
    wheels=5
    def __init__(self) -> None:
        #instance variables
        self.millage=9
        self.campany="Tata"
    
c1=car()
c1.millage=7
c2=car()
#accessing the static variables can be done with class name or object name
print(c1.millage, c1.campany, car.wheels)
print(c2.millage, c2.campany, c2.wheels)
