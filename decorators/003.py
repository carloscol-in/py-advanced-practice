"""
Decorators with arguments
"""

from datetime import datetime, timedelta
import typing


def execution_time(*args, **kwargs):
    """
    Measures and prints the time it takes to execute a function.

    Args:
        return_time_elapsed (bool): Boolean to know if the method should return the time elapsed
    """
    return_time_elapsed = kwargs.get('return_time_elapsed', False)

    def execution_time_wrapper(func: typing.Callable):

        def wrapper(*args, **kwargs) -> typing.Optional[timedelta]:
            """Measure initial datetime, execute the function, get end datetime, and perform logic.

            Returns:
                Optional[datetime]: The time it took to run the function.
            """
            init_time = datetime.now()

            count = func(*args, **kwargs)
            
            end_time = datetime.now()
            time_elapsed = end_time - init_time

            if (return_time_elapsed):
                return time_elapsed, count
            else:
                print(f'Time elapsed: {time_elapsed} seconds')

        return wrapper

    return execution_time_wrapper


@execution_time(return_time_elapsed=True)
def count_to_n(n: int):
    count = 0
    for i in range(n):
        count = i

    return count

def count_to_x(n: int):
    count = 0
    for i in range(n):
        count = i

    return count


"""
Using '@' character."""
print(count_to_n(1000000))

"""
How the use of that character works"""
first = execution_time(return_time_elapsed=True)
second = first(count_to_x)
print(second(1000000))