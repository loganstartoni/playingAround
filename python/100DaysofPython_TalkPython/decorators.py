from functools import wraps
import time


# The framework of a decorator
def mydecorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # do something before the function is called
        # call the function with args
        result = function(*args, **kwargs)
        # do something after the function is called
    # return wrapper = decorated function
    return wrapper

@mydecorator
def my_function(args):
    pass

# could also be written as
# my_function = mydecorator(my_function)

# Interesting link: https://docs.python-guide.org
# for interesting info args and kwargs = http://docs.python-guide.org/en/latest/writing/style/#function-arguments


def show_args(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print('hi from decorator - args:')
        print(args)
        result = function(*args, **kwargs)
        print('hi again from decorator - kwargs:')
        print(kwargs)
        return result
    # return wrapper as a decorated function
    return wrapper


@show_args
def get_profile_dec(name, active=True, *sports, **awards):
    print('\n\thi from the get_profile function\n')


def get_profile(name, active=True, *sports, **awards):
    print('\n\thi from the get_profile function\n')


print("without decorator\n", "-".center(20, "-"))
get_profile('bob', True, 'basketball', 'soccer',
            pythonista='special honor of the community', topcoder='2017 code camp')


print("with decorator\n", "-".center(20, "-"))
get_profile_dec('bob', True, 'basketball', 'soccer',
            pythonista='special honor of the community', topcoder='2017 code camp')
print("-".center(20, "-"), "\n")


# Timeit decorator
def timeit(function):
    @wraps(function)
    def wrapper(*args, **kwargs):

        # Before Tasks
        print("== Starting Timer")
        start = time.time()

        # call function
        function(*args, **kwargs)

        # After Tasks
        end = time.time()
        print(f"== {function.__name__} took {int(end-start)} seconds to complete.")
    return wrapper


def timeit_wrapsless(function):
    def wrapper(*args, **kwargs):

        # Before Tasks
        print("== Starting Timer")
        start = time.time()

        # call function
        function(*args, **kwargs)

        # After Tasks
        end = time.time()
        print(f"== {function.__name__} took {int(end-start)} seconds to complete.")
    return wrapper


def generate_report():
    '''Function to generate revenue report'''
    time.sleep(2)
    print('(actual function) Done, report links ...')


generate_report()


@timeit
def generate_report_dec():
    '''Function to generate revenue report'''
    time.sleep(2)
    print('(actual function) Done, report links ...')


@timeit_wrapsless
def generate_report_dec2():
    '''Function to generate revenue report'''
    time.sleep(2)
    print('(actual function) Done, report links ...')


generate_report_dec()

print(1, generate_report.__doc__)
print(2, generate_report_dec.__doc__)
print(3, generate_report_dec2.__doc__)


# stacking decorators

def print_args(func):
    '''Decorator to print function arguments'''

    @wraps(func)
    def wrapper(*args, **kwargs):

        # before
        print()
        print('*** args:')
        for arg in args:
            print(f'- {arg}')

        print('**** kwargs:')
        for k, v in kwargs.items():
            print(f'- {k}: {v}')
        print()

        # call func
        func(*args, **kwargs)

    return wrapper


parameters = dict(split_geos=True, include_suborgs=False, tax_rate=33)


@timeit
@print_args
def generate_report_args(*months, **parameters):
    time.sleep(2)
    print('(actual function) Done, report links ...')


generate_report_args('October', 'November', 'December', **parameters)

# common uses of decorators
# for websites checking for is a user logged in


# extra example
# make html
def make_html(tag):
    def decorate(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            output = f"<{tag}>"
            output = output + function(*args, **kwargs)
            output = output + f"</{tag}>"
            return output
        return wrapper
    return decorate


@make_html("p")
@make_html("strong")
def get_text(text):
    return text

print(get_text("This is a bold statement."))
