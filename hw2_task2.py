import sys
from datetime import datetime


def timed_output(function):
    original_write = sys.stdout.write

    def wrapper(*args, **kwargs):

        def my_write(string_text):
            if len(string_text.rstrip()):
                timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
                original_write(f"{timestamp}: {string_text}")

        sys.stdout.write = my_write
        result = function(*args, **kwargs)
        sys.stdout.write = original_write
        return result

    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


if __name__ == '__main__':
    print_greeting("Nikita")
