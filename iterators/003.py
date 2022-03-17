"""
Fibonacci iterator class."""

class FibonacciIterator:
    """Fibonacci iterator class.
    """

    def __init__(self, max_value: int = None):
        """You can pass a value where the iterator will stop working on.

        Args:
            max_value (int, optional): The maximum value the iterator can reach. Defaults to None.
        """
        self._max = max_value

    def __iter__(self):
        self._prev, self._curr = None, -1

        return self

    def __next__(self):
        if (self._max != None and self._curr >= self._max):
            raise StopIteration

        if (self._prev != None):
            self._prev, self._curr = self._curr, self._curr + self._prev
        else:
            self._prev, self._curr = abs(self._curr), self._curr + 1

        return self._curr


if __name__ == '__main__':
    # used to know if program should continue
    # looping through the iterator
    should_continue = True
    
    fi = FibonacciIterator()

    for idx, i in enumerate(fi):
        print(i)

        if (idx > 0 and idx % 10 == 0):
            should_continue = input('\nDo you want to continue executing? (Y/N) - ').lower().strip() == 'y'
            print('')

        if (not should_continue):
            break