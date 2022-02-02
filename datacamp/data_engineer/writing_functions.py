import inspect


# Retrieve doc strings
def the_answer():
    """Return the answer to life,
    the universe, and everything.

    Returns:
        int
    """
    return 42


print(the_answer.__doc__)

# use inspect module
print(inspect.getdoc(the_answer))
