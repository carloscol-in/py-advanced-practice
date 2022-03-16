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
        self._prev = None
        self._curr = -1
        self._next = 1

        return self

    def __next__(self):
        if (self._curr >= self._max):
            raise StopIteration

        if (self._prev != None):
            tmp = self._curr
            self._curr += self._prev
            self._prev = tmp
        else:
            self._prev = abs(self._curr)
            self._curr += self._next

        return self._curr


fi = FibonacciIterator(34)
for i in fi:
    print(i)