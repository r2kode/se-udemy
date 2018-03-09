my_list = [1, 2, 3, 4]
my_file = open('firstfile.txt', 'w')

for item in my_list:
    my_file.write(str(item))

my_file.close()