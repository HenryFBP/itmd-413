import os
import random
import time
import datetime

file_path = os.path.join(os.path.dirname(__file__), 'data.txt')

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR


def delete_file(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        pass


def unix_timestamp_to_human_date(timestamp: int) -> str:
    return datetime.datetime.fromtimestamp(timestamp) \
        .strftime('%Y-%m-%d %H:%M:%S')


def append_to_file(path, data):
    with open(path, 'a') as f:
        for datum in data:
            f.write(datum)


def random_unix_timestamp(maxoffset=(5 * HOUR)):
    i = time.time() + random.randint(-maxoffset, maxoffset)
    return int(i)


def random_datum(min=0, max=10, cols=2, separator=' '):
    lst = [random.randint(min, max) for i in range(cols)]

    lst.append(random_unix_timestamp())

    lst = [str(item) for item in lst]

    return separator.join(lst)


def print_stock(start, end, date):
    timestamp = unix_timestamp_to_human_date(date)
    diff = start - end

    print(timestamp, end='')
    print(f": Opened at {start:2}, closed at {end:2}: ", end='')
    print(f"{'+' if diff >= 0 else ''}{diff}")


def read_and_print_stocks(path):
    data = []

    with open(path, 'r') as f:
        for line in f:
            try:
                dataline = line.split(' ')

                if len(dataline) < 3:
                    raise ValueError

                opened = int(dataline[0])
                closed = int(dataline[1])
                unix = int(dataline[2])

                data.append([opened, closed, unix,])
                print(data[-1])
            except ValueError:
                pass  # must be a column...

    data.sort(key=lambda x: x[2])  # sort by date

    for datum in data:
        print_stock(datum[0], datum[1], datum[2])

if __name__ == '__main__':

    delete_file(file_path)

    append_to_file(file_path, 'OPEN CLOSE UNIX_DATE\n')

    for i in range(30):
        datum = random_datum()
        print(datum)
        append_to_file(file_path, datum + '\n')

    read_and_print_stocks(file_path)
