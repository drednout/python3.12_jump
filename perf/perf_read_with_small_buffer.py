import sys
import argparse


def wc(file_object, buf_size):
    char_count = 0
    line_count = 0
    while True:
        data = file_object.read(buf_size)
        if not data:
            break
        line_count += data.count('\n')
        char_count += len(data)

    return line_count, char_count

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-f',
        '--path-to-file',
        type=str,
        help='Path to file for counting chars',
    )
    parser.add_argument(
        '-s',
        '--buf-size',
        default=128,
        type=int,
        help='Buffer size for reading data',
    )
    # parse command line arguments
    args = parser.parse_args()

    if args.path_to_file:
        file_object = open(args.path_to_file, 'r')
    else:
        file_object = sys.stdin

    line_count, char_count = wc(file_object, args.buf_size)
    file_object.close()

    print(f'Line count: {line_count}')
    print(f'Char count: {char_count}')
