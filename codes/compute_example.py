import datetime
import multiprocessing
from threading import Thread
import math


def do_math(start=0, num=10):
    print(f'start: {start} ----------- num: {num} ////')
    position = start
    random_number = 1000 * 1000
    while position < num:
        position += 1
        math.sqrt((position - random_number) ** 2)


def main():
    t0 = datetime.datetime.now()

    threads = []
    processor_count = multiprocessing.cpu_count()
    for n in range(1, processor_count + 1):
        threads.append(
            Thread(
                target=do_math,
                kwargs={
                    'start': 50_000_000 * (n - 1) / processor_count,
                    'num': 50_000_000 * n / processor_count
                },
                daemon=True
            )
        )

    [t.start() for t in threads]
    [t.join() for t in threads]

    dt = datetime.datetime.now() - t0
    print(f'Done in {dt.total_seconds()} seconds')


if __name__ == '__main__':
    main()