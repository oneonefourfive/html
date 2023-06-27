class Animal:
    def __init__(self,name):
        self.name = name
    def show_info(self):
        return "animal name:{0}".format(self.name)
    def move(self):
        print(" move one move...")
class Cat(Animal):
    def __init__(self, name,age):
        super().__init__(name)
        self.age=age
Catt = Cat('daodao',1.5)
Catt.move()
print(Catt.show_info())


