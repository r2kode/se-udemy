def sum_num(a, b):
    """
    Returns sum of two numbers
    :param a: numeric
    :param b: numeric
    :return: numeric
    """
    return a + b


def is_metro(city):
    l = ['sfo', 'nyc', 'la']

    if city in l:
        return True
    else:
        return False


def optional_params(a, b, c=3):
    """
    Usage of positional(optional) parameters
    :param a:
    :param b:
    :param c:
    :return:
    """
    return a + b + c


print(optional_params(1, 2))
print(sum_num(2, 2))

x = is_metro('pszczyna')
print(x)

someVariable = 'Stefan'
