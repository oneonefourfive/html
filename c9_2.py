class Car:
    def __init__(self,name,age,sex = '雌性'):
        self.name = name
        self.age = age
        self.sex = sex
car = Car('球球',2)
cra = Car('haha',2,'boy')
arc = Car(name = 'tuo bu',age = 3, sex = 'walmart bag')
print('我们家车叫{0},{1}岁了, is a {2}'.format(car.name,car.age,car.sex))
print('我们家车叫{0},{1}岁了, is a {2}'.format(cra.name,cra.age,cra.sex))
print('我们家车叫{0},{1}岁了, is a {2}'.format(arc.name,arc.age,arc.sex))