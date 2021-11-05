from exec_timer import exec_timer
import time

def sleep_seconds(seconds, text="sleep seconds has finished"):
    """Example function to be tested by exec_timer, it sleeps for the given seconds and prints a given text."""
    time.sleep(seconds)
    print(text)

if __name__ == "__main__":
    # examples of how to use exec_timer function
    exec_timer(sleep_seconds,2, text="function finished")
    exec_timer(sleep_seconds,5)