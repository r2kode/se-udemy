x = 0
while x < 10:
    print('Value of x is: {}'.format(x))
    x += 1

l = []
num = 0
while num < 10:
    l.append(num)
    num += 1

print('Can I prnt a list with format()?\n{}'.format(l))

i = 0
while i < 10:
    print('i = {}'.format(i))
    i += 1
    if i == 8:
        print('Here loop breaks')
        break
    print('Something before break')

j = 10
while j > 0:
    print('{} inter of loop'.format(j))
    j -= 1
else:
    print('some code in else, will not execute if loop hit break')

my_string = 'yippee-ki-yay'
for c in my_string:
    if c == 'y':
        print(c.upper(), end=' ')
    else:
        print(c, end=' ') # end='' replace the end of line

print('\ndealing with lists')
cars = ['mazda', 'subaru', 'lexus']
for car in cars:
    print(car.capitalize())

d = {1: 'one', 2: 'two', 'stefan': 35}
print(d)
for key, val in d.items():
    print('key = {}, value = {}'.format(key,val))


# Zip function

l1 = [1,2,3,4,5,6,7]
l2 = ['item1', 'item2', 'item3']

for a, b in zip(l1,l2):
    print('item from l1: {}, item from l2: {}'.format(a, b))

zip_object = zip(l1 ,l2)
print(zip_object)

# range function
new_range = range(0, 50, 2)
print('by itself range() in py3 do NOT generate list')
print(new_range)
print(type(new_range))
print('to save generated number range has to be wrapped in list() funstion')
print(list(new_range))

some_list = [1,23,4,5,6,7,8]
for num in range(0, 4):
    print(num)