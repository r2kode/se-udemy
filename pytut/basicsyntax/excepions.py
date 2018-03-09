def exception_handling():
    try:
        a = 10
        b = 55
        c = 0
        d = (a + b) / c

        print(d)
    except ZeroDivisionError as e:
        print('something goes wrong \n{}'.format(e))
        raise Exception('this is the exception')
    except TypeError as e:
        print('Type error\n{}'.format(e))
    else:
        print('if no exceptions else is executed')
    finally:
        print('Finally always executes')


exception_handling()