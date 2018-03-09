class Car(object):

    def __init__(self):
        print('New car created')

    def drive(self):
        print('car started')

    def stop(self):
        print('car stoped')


class Subaru(Car):

    def __init__(self):
        Car.__init__(self)
        print('Subaru created')

    def drive(self):
        super(Subaru, self).drive()
        print('Subaru drives')

    def dive_type(self):
        print('AWD')


car_one = Car()
car_one.drive()
car_one.stop()
subaru = Subaru()
subaru.drive()
subaru.stop()