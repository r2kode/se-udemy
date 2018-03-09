

def exception_excercise(car, key):
    try:
        print(car[key])
    except KeyError as e:
        print('no key: "color"\n{}'.format(e))
        # raise Exception('key not found')


car = {
    'make': 'Subaru',
    'model': 'Legacy',
    'year': 2004
}

exception_excercise(car, 'color')