import sys

if __name__ == '__main__':
    n = 100000
    if len(sys.argv) > 1:
        n = int(sys.argv[1])

    for i in range(n):
        print(f'ERROR:root:one more error message {i}')
