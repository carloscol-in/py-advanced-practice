def simple_generator():
    """Simple generator function.

    See how the state of `some_random_var` is kept through the generator's lifecycle

    Yields:
        int: Some random variable that gets changed on every `next()` call.
    """

    print('Step 1')
    some_random_var = 4

    yield some_random_var

    print('Step 2')
    some_random_var += 13

    yield some_random_var

    print('Step 3')
    some_random_var -= 8

    yield some_random_var


# sg = simple_generator()

# print(next(sg))
# print(next(sg))
# print(next(sg))
# print(next(sg))

for s in simple_generator():
    print(s)