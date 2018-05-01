import os
import random
import time

file_path = os.path.join(os.path.dirname(__file__), 'data.txt')

SECOND = 1000
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE


def delete_file(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        pass


def append_to_file(path, data):
    with open(path, 'a') as f:
        for datum in data:
            f.write(datum)


def random_unix_timestamp(maxoffset=(30 * MINUTE)):
    i = time.time() + random.randint(-maxoffset, maxoffset)
    return int(i)


def random_datum(min=0, max=10, cols=2, separator=' '):
    lst = [random.randint(min, max) for i in range(cols)]

    lst.append(random_unix_timestamp())

    lst = [str(item) for item in lst]

    return separator.join(lst)


if __name__ == '__main__':

    delete_file(file_path)

    append_to_file(file_path, 'OPEN CLOSE UNIX_DATE\n')

    for i in range(3):
        datum = random_datum()
        print(datum)
        append_to_file(file_path, datum + '\n')
