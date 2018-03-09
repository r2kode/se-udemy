class Fruit:

    def __init__(self):
        print('init fuit')

    def nutrition(self):
        print('fruit nutrition value')

    def fruit_shapes(self):
        print('fruit shape')


class Orange(Fruit):

    def __init__(self):
        Fruit.__init__(self)
        print('init orange')

    def nutrition(self):
        print('nutrition value of orange')

    def color(self):
        print('color of orange')


fruit = Fruit()
orange = Orange()

fruit.nutrition()
fruit.fruit_shapes()
orange.nutrition()
orange.color()
orange.fruit_shapes()