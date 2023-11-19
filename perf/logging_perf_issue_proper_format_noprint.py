import logging
import sys

class ObjectForLog:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'ObjectForLog(x={self.x}, y={self.y}, z={self.z})'

    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    n = 10000000
    if len(sys.argv) > 1:
        n = int(sys.argv[1])

    o_for_log = ObjectForLog(100, 500, 0)
    for i in range(n):
        logging.debug('one more error message %s', o_for_log)
