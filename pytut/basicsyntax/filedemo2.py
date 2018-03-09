with open('withas.txt', 'w') as my_file:
    my_file.write('some text that should go into the file')


print('\n --- reading file ---- \n')
with open('withas.txt', 'r') as my_file:
    print(my_file.read())
