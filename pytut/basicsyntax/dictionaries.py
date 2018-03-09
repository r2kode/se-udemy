car = {
    'make': 'subaru',
    'model': 'is250',
    'year': 2012
}

d = {}

print(car)

print(car['model'])

d['one'] = 1
d['two'] = 2
d[3] = 'tree'

print(d.keys())
print(d.values())
print(d.items())
for key, value in d.items():
    print('{} => {}'.format(key, value))

