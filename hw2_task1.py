import sys
from datetime import datetime


original_write = sys.stdout.write


def my_write(string_text):
    if len(string_text.rstrip()):
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        original_write(f"{timestamp}: {string_text}")


sys.stdout.write = my_write


if __name__ == '__main__':
    print('1, 2, 3')
