"""
You can build an iterator by using a class
with at least methods `__iter__`, and `__next__`"""

class EvenNumbers:
    """Generate all even numbers up to the max value passed
    into the class' constructor.
    """

    def __init__(self, max_value: int = None):
        self._max = max_value

    def __iter__(self):
        self._num = 0
        return self

    def __next__(self):
        if not self._max or self._num <= self._max:
            result = self._num
            self._num += 2
            return result
        else:
            raise StopIteration

for en in EvenNumbers(20):
    print(en)