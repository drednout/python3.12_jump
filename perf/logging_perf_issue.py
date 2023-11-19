import logging
import sys

if __name__ == '__main__':
    n = 100000
    if len(sys.argv) > 1:
        n = int(sys.argv[1])

    for i in range(n):
        logging.error(f'one more error message {i}')
