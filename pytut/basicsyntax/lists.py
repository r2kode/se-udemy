cars = ['mazda', 'lexus', 'subaru']
empty_list = []
print('*' * 20)

cars.append('carisma')
cars.insert(1, 'laguna')
print(len(cars))
print(cars)
print(cars.index('subaru'))
while cars:
    print(cars.pop())

print(range(5))