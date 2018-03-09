class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def getCarInfo(self):
        return 'Make: {}, model: {}'.format(self.make, self.model)


car_one = Car('Subaru', 'WRX STI')
print(car_one.getCarInfo())


car_two = Car('Mazda', '6')
print(car_two.getCarInfo())
