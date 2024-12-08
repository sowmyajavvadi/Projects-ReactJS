class Computer:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def config(self):
       
        print("addition is:", self.a+self.b)
com1=Computer(12, 6)
com2=Computer(5,8)

com1.config()
com2.config()
