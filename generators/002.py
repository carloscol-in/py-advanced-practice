"""
Fibonacci iterator class."""


def fibonacci_generator(max_value: int = None):
    """Fibonacci iterator function.
    """

    c, n = 0, 1

    while True:

        yield c

        c, n = c + n, c


if __name__ == '__main__':
    # used to know if program should continue
    # looping through the iterator
    should_continue = True

    fi = fibonacci_generator()

    for idx, i in enumerate(fi):
        print(i)

        if (idx > 0 and idx % 10 == 0):
            should_continue = input(
                '\nDo you want to continue executing? (Y/N) - ').lower().strip() == 'y'
            print('')

        if (not should_continue):
            break
