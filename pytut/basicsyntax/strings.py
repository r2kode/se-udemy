some_string = "yippeekiyay"
another_string = "yay"

print(some_string)
print(another_string)

print(some_string[::-1])
print(some_string.split('i'))
print(some_string.replace('i', 'i-'))
print(some_string.__len__())

new_string = ''

for index in range(len(some_string)-1, -1, -1):
    # print(some_string[index])
    new_string += some_string[index]

print(new_string)