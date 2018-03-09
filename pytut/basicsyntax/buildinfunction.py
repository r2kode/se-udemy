def largest_num(*args):
    """
    *args - allows to pass multiple arguments
    :param args:
    :return:
    """
    return max(args)


def smallest_num(*args):
    return min(args)


def abs_function(a):
    return abs(a)


print(largest_num(2, 3, 10, -1, 100))
print(smallest_num(2, 3, 10, -1, 100))
print(abs(-20))
print(abs(20))
print(type(99))
print(type(0.2))
print(type('999'))
print(type(['a', '23', 'asdad', 0]))
