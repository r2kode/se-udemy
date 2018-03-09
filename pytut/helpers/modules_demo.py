# import app.car as car
from app.car import info


class CarModuleDemo:

    def car_description(self, make, model):
        info(make, model)


car_demo = CarModuleDemo()
car_demo.car_description('zlom', 'zlom')