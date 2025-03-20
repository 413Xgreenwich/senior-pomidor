def my_decorator(func):
    def wrapper():
        print('[TRACE] Function starting')
        func()
        print('[TRACE] Function ends')
    return wrapper


@my_decorator
def my_func():
    print('[INFO] Function my_func working . . .')


my_func()

