"""
Decorators using '@' character.
"""

from datetime import datetime

def execution_time(func):
    """Measure how much it takes for a function to execute.

    Args:
        func (typing.Callable): Function to measure execution time of.
    """
    def wrapper(*args, **kwargs):
        init_time = datetime.now()
        func(*args, **kwargs)
        end_time = datetime.now()
        time_elapsed = end_time - init_time
        print(f'Time elapsed: {time_elapsed} seconds')

    return wrapper

@execution_time
def count_to_n(n: int):
    count = 0
    for i in range(n):
        count += i

count_to_n(1000000)
