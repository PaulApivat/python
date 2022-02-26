
# double_args decorator
# Breakdown of how Decorator works


# deocrator function must define a new function
# decorator is a wrapper that returns what the first function passed it, while modifying behavior
import signal
from functools import wraps
from collections import defaultdict
import time


def double_args(func):
    def wrapper(a, b):
        return func(a * 2, b * 2)
    return wrapper


def multiply(a, b):
    return a * b

# instead of assigning to new variable, overwrite
# new_multiply = double_args(multiply)


multiply = double_args(multiply)

print(multiply(1, 5))

# python stores the new multiply() in the original multiply()'s closure
multiply.__closure__[0].cell_contents

# decorating the multiply() function with @double_args


@double_args
def multiply(a, b):
    return a * b


print("using @double_args: ", multiply(1, 5))


# print_before_and_after()
def print_before_and_after(func):
    def wrapper(*args):
        print('Before {}'.format(func.__name__))
        # Call the function being decorated with *args
        func(*args)
        print('After {}'.format(func.__name__))
    # Return the nested function
    return wrapper


@print_before_and_after
def multiply(a, b):
    print(a * b)


multiply(5, 10)


# Time Decorator
def timer(func):
    """A decorator that prints how long a function took to run."""
    # Define the wrapper function in return
    def wrapper(*args, **kwargs):
        # When wrapper() is called, get the current time
        t_start = time.time()
        # Call the decorated function and store the result
        result = func(*args, **kwargs)
        # Get the total time it took to run, and print it.
        t_total = time.time() - t_start
        print('{} took {}s'.format(func.__name__, t_total))
        return result
    return wrapper

# Using timer() decorator


@timer
def sleep_n_seconds(n):
    time.sleep(n)


sleep_n_seconds(5)


# ------------- Print the return Type -----------------#

def print_return_type(func):
    # Define wrapper(), the decorated function
    def wrapper(*args, **kwargs):
        # Call the function being decorated
        result = func(*args, **kwargs)
        print('{}() returned type {}'.format(
            func.__name__, type(result)
        ))
        return result
    # Return the decorated function
    return wrapper


@print_return_type
def foo(value):
    return value


print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))


# ----------------- Counter ----------------#
def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        # Call the function being decorated and return the result
        return wrapper.count
    wrapper.count = 0
    # Return the new decorated function
    return wrapper

# Decorate foo() with the counter() decorator


@counter
def foo():
    print('calling foo()')


foo()
foo()

print('foo() was called {} times.'.format(foo.count))

# -------- Using wraps from functools to preserve METADATA ----------- #


def add_hello(func):
    # Decorate wrapper() so that it keeps func()'s metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Print 'hello' and then call the decorated function."""
        print('Hello')
        return func(*args, **kwargs)
    return wrapper


@add_hello
def print_sum(a, b):
    """Adds two numbers and prints the sum"""
    print(a + b)


print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)

# ------------- Decorator Factory: Example 1 -------------- #


def run_n_times(n):
    """Define and return a decorator"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@run_n_times(3)
def print_sum(a, b):
    print(a + b)


@run_n_times(5)
def print_hello():
    print('Hello!')


# ------------- Decorator Factory: Example 2 -------------- #


def timeout(n_seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # set an alarm for n seconds
            signal.alarm(n_seconds)
            try:
                # Call the decorated func
                return func(*args, **kwargs)
            finally:
                # Cancel alarm
                signal.alarm(0)
        return wrapper
    return decorator

# -------- Decorator to Tag Functions ----------#


def tag(*tags):
    # Define a new decorator, named "decorator", to return
    def decorator(func):
        # Ensure the decorated function keeps its metadata
        @wraps(func)
        def wrapper(*args, **kwargs):
          # Call the function being decorated and return the result
            return func(*args, **kwargs)
        wrapper.tags = tags
        return wrapper
    # Return the new decorator
    return decorator


@tag('test', 'this is a tag')
def foo():
    pass


print(foo.tags)

# ----------- Decoratory  for returning variable type ------------#


def returns(return_type):
    # Complete the returns() decorator
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            assert type(result) == return_type
            return result
        return wrapper
    return decorator


@returns(dict)
def foo(value):
    return value


try:
    print(foo([1, 2, 3]))
except AssertionError:
    print('foo() did not return a dict!')


# ----Do not call ----Memoizing Decorator -------------------------#
# ------------- Produces TypeError: unhashable type: 'dict' ----------#
def memoize(func):
    """Store the results of the decorated function for fast lookup
    """
    # Store results in a dict that maps arguments to results
    cache = {}
    # Define the wrapper function to return.

    def wrapper(*args, **kwargs):
        # If these arguments haven't been seen before,
        if (args, kwargs) not in cache:
            # Call func() and store the result.
            cache[(args, kwargs)] = func(*args, **kwargs)
        return cache[(args, kwargs)]
    return wrapper


@memoize
def slow_function(a, b):
    print('Sleeping...')
    time.sleep(5)
    return a + b
