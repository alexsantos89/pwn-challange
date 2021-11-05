import time
from datetime import timedelta

def exec_timer(func, *args, **kwargs):
    """
    Compute how long it takes to run a given function and respective arguments.
    Print in a friendly format how long it takes.

    :param func: function to be executed and have its performance evaluated
    :param args: all non keyword arguments will be provided to the function
    :param kwargs: all keyword arguments will be provided to the function
    """
    tic = time.perf_counter()
    result = func(*args, **kwargs)
    toc = time.perf_counter()
    duration = timedelta(seconds=toc-tic)
    print("It took: {hours} hours, {minutes} minutes, {seconds} seconds, {microseconds} microseconds".
            format(hours = duration.seconds//3600,
                   minutes = (duration.seconds//60)%60,
                   seconds = (duration.seconds%60),
                   microseconds = duration.microseconds))
    return result